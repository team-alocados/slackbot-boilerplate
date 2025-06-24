from loguru import logger
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackAPI:

    def __init__(self, token: str = None):
        self.client = WebClient(token=token)

    def oauth_v2_access(
        self, client_id: str = None, client_secret: str = None,
        code: str = None, redirect_uri: str = None
    ):
        return self.client.oauth_v2_access(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            redirect_uri=redirect_uri
        )

    def views_publish(self, block: dict, user_id: str):
        try:
            return self.client.views_publish(
                user_id=user_id,
                view=block,
            )
        except SlackApiError as e:
            raise e

    def chat_post_message(
        self, channel: str, text: str, block: dict = None,
        thread_ts: str = None
    ):
        try:
            return self.client.chat_postMessage(
                channel=channel,
                text=text,
                blocks=block,
                thread_ts=thread_ts
            )
        except SlackApiError as e:
            logger.error(f"chat_posstMessage failed: {e.response['error']}")
            raise e

    def views_open(self, view: dict, trigger_id: str):
        try:
            return self.client.views_open(
                trigger_id=trigger_id,
                view=view
            )
        except SlackApiError as e:
            logger.error(f"views_open failed: {e.response['error']}")
            raise e

    def views_update(self, view_id: str, view: dict):
        try:
            return self.client.views_update(
                view_id=view_id,
                view=view
            )
        except SlackApiError as e:
            logger.error(f"views_update failed: {e.response['error']}")
            raise e
