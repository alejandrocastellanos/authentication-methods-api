import jwt

from datetime import datetime, timedelta

from src.utils.settings import SECRET_KEY, ALGORITHM


def create_jwt(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    data_copy = data.copy()
    data_copy.update({"exp": datetime.utcnow() + expires_delta})
    return jwt.encode(data_copy, SECRET_KEY, algorithm=ALGORITHM)
