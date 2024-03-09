from pydantic import BaseModel


class PostSchema(BaseModel):

    track: int|str

