class ErrorLog:

    def __init__(
        self,
        app_name: str,
        endpoint: str = None,
        status_code: str = None,
        payload: str = None,
        description: str = None
    ):
        self.block = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": ":bangbang: 에러가 감지되었습니다!",
                        "emoji": True,
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*발생 대상*: {app_name}"
                    }
                },
            ]
        }

        if endpoint:
            self.block['blocks'].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*엔드포인트*: {endpoint}"
                }
            })
        if status_code:
            self.block['blocks'].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*상태 코드*: {status_code}"
                }
            })
        if payload:
            self.block['blocks'].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*페이로드*"
                }
            })
            self.block['blocks'].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```{payload.replace('`', '')}```"
                }
            })
        if description:
            self.block['blocks'].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*세부 설명*"
                }
            })
            self.block['blocks'].append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": description
                }
            })
