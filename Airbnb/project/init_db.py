from db.session import Base, engine
from db.models import User, OTP

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Tables created ✅")
