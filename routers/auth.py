from sqlalchemy.orm import Session
from database import get_db
import schemas, utils, models, auth_config as oauth2
from fastapi import Depends, status, HTTPException, APIRouter, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Login"])


# Login user
@router.post("/login")
def login(
    admin_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    #  Not using schema for validating email, password
    # Instead using OAuth2PasswordRequestForm for validation
    admin = (
        db.query(models.Admin)
        .filter(
            models.Admin.username == admin_credentials.username,
        )
        .first()
    )
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    if not utils.verify(admin_credentials.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    # Creating a JWT Token
    token = oauth2.create_token(data={"username": admin.username})
    response_data = {"message": "Logged in successfully", "data": {"token": token}}
    response = JSONResponse(response_data)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=False,
        max_age=oauth2.TOKEN_EXPIRY_MINUTES * 60,  # Token expiration in seconds
        # expires=datetime.now(timezone.utc)+ timedelta(minutes=oauth2.TOKEN_EXPIRY_MINUTES),
        samesite="none",
        # secure=True,  # Uncomment this line for HTTPS only
    )
    return response


@router.post("/logout")
async def logout(
    response: Response, admin: models.Admin = Depends(oauth2.get_current_admin)
):
    response.delete_cookie(key="access_token")
    return {"message": "Logged out successfully"}
