from pydantic import BaseModel


class PutSchema(BaseModel):

    ok: bool


class ErrorSchema(BaseModel):
    
    message: str
    
