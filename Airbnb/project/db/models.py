from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import CHAR  # optional for UUID
from datetime import datetime
import uuid
from db.session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(String(50), default="guest")
    created_at = Column(DateTime, default=datetime.utcnow)

class OTP(Base):
    __tablename__ = "otp_codes"
    email = Column(String(255), primary_key=True)
    code = Column(String(6), nullable=False)
    expires_at = Column(DateTime, nullable=False)
