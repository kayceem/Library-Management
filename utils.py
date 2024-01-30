import models
from sqlalchemy.orm import Session


def check_user(db: Session, id: str):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    return user


def check_conflicts(db: Session, email: str = None, **kwargs):
    existing_user = (
        db.query(models.User)
        .filter(
            models.User.email == email,
        )
        .first()
    )
    return existing_user
