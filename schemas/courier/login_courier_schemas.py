from pydantic import BaseModel


class PostOkSchema(BaseModel):

    id: int|str


class PostErrorSchema(BaseModel):

    message: str
