from typing import Optional
from sqlmodel import Field

from todo.utils import TimestamppedModel
from todo.security import HashedPassword


class User(TimestamppedModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    email: str = Field(nullable=False, unique=True)
    username: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)
    password: HashedPassword = Field(nullable=False)
