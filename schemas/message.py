from pydantic import BaseModel


class MessageSchema(BaseModel):
    text: str


class MessageResponse(BaseModel):
    number: int
    text: str