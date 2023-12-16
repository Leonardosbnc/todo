from datetime import date

from typing import Optional
from uuid import uuid4, UUID
from sqlmodel import Field, Column, Enum

from todo.enums.todo_status import Status
from todo.utils import TimestamppedModel


class Todo(TimestamppedModel, table=True):
    id: UUID = Field(primary_key=True, nullable=False, default_factory=uuid4)
    name: str = Field(nullable=False)
    status: Status = Field(sa_column=Column(Enum(Status)), default=Status.IN_PROGRESS)
    group: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    estimated_date: Optional[date] = Field(default=None)
    max_date: Optional[date] = Field(default=None)
    notify: bool = Field(default=False)
