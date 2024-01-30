from typing import List
from database import get_db
from sqlalchemy.orm import Session
import schemas, models, utils, auth_config as oauth2
from fastapi import Depends, status, HTTPException, APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


# Get all users
@router.get("/", response_model=List[schemas.UserResponse])
async def get_users(
    db: Session = Depends(get_db),
    admin: models.Admin = Depends(oauth2.get_current_admin),
):
    users = db.query(models.User).all()
    return users


# Get user with id
@router.get("/{user_id}", response_model=schemas.UserResponse)
async def get_user_by_id(
    user_id: str,
    db: Session = Depends(get_db),
    admin: models.Admin = Depends(oauth2.get_current_admin),
):
    user = utils.check_user(db=db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


# Create user
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse
)
async def create_user(
    user: schemas.UserBase,
    db: Session = Depends(get_db),
    admin: models.Admin = Depends(oauth2.get_current_admin),
):
    conflicts = utils.check_conflicts(db, **user.dict())

    if conflicts:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    new_user = models.User(**user.dict())  # Unpcak dictionary
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
