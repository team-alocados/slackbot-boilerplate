from fastapi import Depends

from app.depends.slack import command_verify_request
from app.response import ok
from . import slack


@slack.post(
    "/command", tags=["slack"],
)
async def command_handler(
    command: dict = Depends(command_verify_request)
):
    """
    command = {
        'team_id': 'T01M3AVTSTD',
        'channel_id': 'C092HGSMB54',
        'channel_name': 'proj-burning',
        'user_id': 'U03QT45E36E',
        'command': '/coffee',
        'is_enterprise_install': 'false',
        'response_url': 'https://hooks.slack.com/commands/T01M3AVTSTD/9098552549494/3YGh7ag5Bvg6Mech8xCH5tku',
        'trigger_id': '9098552555910.1717369944931.63147d9c9fba6c1c06aeb353bbe83c00'
    }
    """
    print(command)
    return ok()
