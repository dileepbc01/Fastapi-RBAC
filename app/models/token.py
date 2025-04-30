from pydantic import BaseModel
from datetime import timedelta

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub:str
    role:str