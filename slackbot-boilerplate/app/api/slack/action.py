from fastapi import Depends

from app.depends.slack import action_verify_request
from app.response import ok
from . import slack


@slack.post(
    "/action", tags=["slack"],
)
async def action_handler(
    payload: dict = Depends(action_verify_request),
):
    """
    https://api.slack.com/reference/interaction-payloads/block-actions
    """
    print(payload)

    return ok()
