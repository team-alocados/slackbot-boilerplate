from pydantic import BaseModel


class SlackEvent(BaseModel):
    type: str
    token: str
    challenge: str
    