from typing import List
from database import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import utils, auth_config as oauth2, schemas, utils, models
from fastapi import Depends, status, HTTPException, APIRouter, Response

router = APIRouter(prefix="/admin", tags=["Admins"])


# Create admin
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.AdminBase)
async def create_admin(
    admin: schemas.Admin,
    db: Session = Depends(get_db),
):
    # Check if admin exists
    admin_exists = (
        db.query(models.Admin).filter(models.Admin.username == admin.username).first()
    )

    if admin_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    admin.password = utils.hash(admin.password)
    new_admin = models.Admin(**admin.dict())  # Unpcak dictionary
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin
