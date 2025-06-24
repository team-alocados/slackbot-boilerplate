from fastapi import Query
from fastapi.params import Depends
from fastapi.responses import RedirectResponse

from app.depends.module import app_settings
from controller.slack import SlackAPI
from settings import Settings
from . import slack


@slack.get("/oauth/install/callback", tags=["slack"])
async def oauth_install_callback_handler(
    code: str = Query(default=None),
    error: str = Query(default=None),
    settings: Settings = Depends(app_settings)
):
    if error is not None:
        """
        Handle OAuth error
        https://api.slack.com/authentication/oauth-v2#errors
        """
        return RedirectResponse(url="https://example.com")

    if not code:
        """
        Handle missing code
        """
        return RedirectResponse(url="https://example.com")

    slack_api = SlackAPI()
    oauth_response = slack_api.oauth_v2_access(
        client_id=settings.slack_client_id,
        client_secret=settings.slack_client_secret,
        code=code
    )
    """
    oauth_response = {
        "ok": True,
        "app_id": "A092BHS5X9V",
        "authed_user": {"id": "U03RGSZGHCG"},
        "scope": "chat:write,im:write,commands,im:history,team:read,users:read",
        "token_type": "bot",
        "access_token": "token",
        "bot_user_id": "U0930CT06HY",
        "team": {"id": "T023HDBGZQQ", "name": "Colawork_test"},
        "enterprise": None,
        "is_enterprise_install": False
    }
    """

    if not oauth_response["ok"]:
        """
        Handle OAuth response error
        """
        return RedirectResponse(url="https://example.com/error")

    """
    Your DB logic to handle the OAuth installation redirect should go here.
    """

    return RedirectResponse(url="https://example.com/success")
