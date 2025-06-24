from fastapi import Body, Depends

from app.depends.slack import verify_request
from app.response import ok
from . import slack


@slack.post(
    "/event",
    tags=["slack"],
    dependencies=[Depends(verify_request)]
)
async def event_handler(
    type = Body(alias="type", embed=True),
    challenge: str = Body(embed=True, default=None),
):
    if type == 'url_verification':
        return {"challenge": challenge}

    return ok()
