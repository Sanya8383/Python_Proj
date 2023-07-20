from pydantic import BaseModel


class PostResponse(BaseModel):
    code: int
    msg: str


class AddrList(BaseModel):
    address: str
    list: str


class Message(BaseModel):
    message: str
