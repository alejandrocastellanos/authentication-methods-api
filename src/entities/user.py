from typing import Optional

from pydantic import BaseModel


class User(BaseModel):

    id: Optional[str] = None
    email: str
    password: Optional[str] = None
