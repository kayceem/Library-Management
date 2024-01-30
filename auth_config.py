from jose import jwt, JWTError
import schemas, database, models
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from config import settings
from fastapi import Request

# Secret Key used to hash info
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
TOKEN_EXPIRY_MINUTES = 60

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(data: dict):
    to_encode = data.copy()
    iat = datetime.utcnow()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRY_MINUTES)
    to_encode.update({"iat": iat})
    to_encode.update({"exp": expire})
    # Signing JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exceptions, expired_exceptions):
    try:
        # Decoding JWT
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        username = payload.get("username")
        # Check is token has id
        if username is None:
            raise credentials_exceptions
        # Create a token_data class with TokenData Schema
        token_data = schemas.TokenData(username=username)
    # Checks expiry of token
    except jwt.ExpiredSignatureError:
        raise expired_exceptions
    # Checks invalid credentials
    except JWTError as e:
        raise credentials_exceptions
    return token_data

# Returns the current admin logged in
def get_current_admin(request: Request, db: Session = Depends(database.get_db)):
    # For wrong or invalid credentials
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # For expired JWT
    expired_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
    )
    # For when no tokenm is provided
    login_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="User not logged in"
    )

    token = request.cookies.get("access_token")

    # Handels if no token is provided
    if not token:
        raise login_exception

    token = verify_token(token, credentials_exceptions, expired_exception)

    admin = (
        db.query(models.Admin).filter(models.Admin.username == token.username).first()
    )
    # Handels if admin logged in is same as admin in token
    if not admin:
        raise credentials_exceptions
    return admin.username
