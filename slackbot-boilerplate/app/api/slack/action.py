from app.response import ok
from . import slack


@slack.post("/action")
async def action_handler():
    return ok()
