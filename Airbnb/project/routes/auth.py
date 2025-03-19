from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from auth.otp_service import store_otp
from auth.email_sender import send_otp_email
from auth.otp_service import verify_otp
from db import crud



router = APIRouter()

@router.post("/auth/request-otp")
def request_otp(email: str, db: Session = Depends(get_db)):
    otp_record = store_otp(email, db)
    sent = send_otp_email(email, otp_record.code)

    if not sent:
        raise HTTPException(status_code=500, detail="Failed to send OTP")

    return {"message": "OTP sent to your email"}



@router.post("/auth/verify-otp")
def verify_otp_route(email: str, code: str, db: Session = Depends(get_db)):
    valid, message = verify_otp(email, code, db)
    if not valid:
        raise HTTPException(status_code=400, detail=message)

    user = crud.get_user_by_email(db, email)
    if not user:
        user = crud.create_user(db, email)

    return {"message": "Login successful", "user_id": user.id}