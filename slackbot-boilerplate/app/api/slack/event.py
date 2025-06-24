from typing import List

from fastapi import Body, Depends

from app.depends.slack import verify_request
from app.response import ok
from controller.slack import SlackAPI
from . import slack


@slack.post(
    "/event", tags=["slack"],
    dependencies=[Depends(verify_request)]
)
async def event_handler(
    type: str = Body(embed=True),
    event_id: str = Body(embed=True, default=None),
    event: dict = Body(embed=True, default=None),
    team_id: str = Body(embed=True, default=None),
    authorizations: List[dict] = Body(embed=True, default=None),
    challenge: str = Body(embed=True, default=None),
):
    if type == 'url_verification':
        return {"challenge": challenge}

    slack_api = SlackAPI(token=None)
    if event['type'] == "app_home_opened":
        pass

    return ok()
