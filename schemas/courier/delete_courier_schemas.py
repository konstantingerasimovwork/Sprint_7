from pydantic import BaseModel


class DeleteSchema(BaseModel):

    ok: bool


class ErrorSchema(BaseModel):

    message: str
