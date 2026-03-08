from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _validate_password_length(password: str):
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password must be 72 bytes or fewer")


def hash_password(password: str):
    _validate_password_length(password)
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        _validate_password_length(plain_password)
        return pwd_context.verify(plain_password, hashed_password)
    except ValueError:
        return False


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)