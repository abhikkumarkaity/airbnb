from sqlalchemy.orm import Session
from datetime import datetime
from . import models
import uuid


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, email: str):
    new_user = models.User(id=str(uuid.uuid4()), email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_otp(db: Session, email: str, code: str, expires_at: datetime):
    new_otp = models.OTP(
        email=email,
        code=code,
        expires_at=expires_at,
    )
    db.add(new_otp)
    db.commit()
    db.refresh(new_otp)
    return new_otp


def get_latest_otp(db: Session, email: str):
    return (
        db.query(models.OTP)
        .filter(models.OTP.email == email)
        .order_by(models.OTP.expires_at.desc())
        .first()
    )
