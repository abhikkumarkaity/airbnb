from datetime import datetime, timedelta
from db import crud
from auth.otp_utils import generate_otp

def store_otp(email: str, db):
    code = generate_otp()
    expires_at = datetime.utcnow() + timedelta(minutes=10)
    return crud.create_otp(db, email, code, expires_at)


def verify_otp(email: str, code: str, db):
    otp_record = crud.get_latest_otp(db, email)
    if not otp_record:
        return False, "No OTP found"

    if otp_record.code != code:
        return False, "Invalid OTP"

    if otp_record.expires_at < datetime.utcnow():
        return False, "OTP expired"

    # Optional: mark as used
    otp_record.used = True
    db.commit()

    return True, "OTP valid"
