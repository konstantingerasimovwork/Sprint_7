from pydantic import BaseModel


class PostOkSchema(BaseModel):

    ok: bool


class PostErrorSchema(BaseModel):

    message: str
