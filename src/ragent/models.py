import typing
from pydantic import BaseModel


class Reference(BaseModel):
    id: str
    text: str
    title: str


class Answer(BaseModel):
    id: str
    text: str
    references: typing.List[Reference]
