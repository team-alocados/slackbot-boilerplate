from app.response import ok
from . import slack


@slack.post("/command")
async def command_handler():
    return ok()
