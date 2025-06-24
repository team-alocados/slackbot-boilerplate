from typing import Optional

import requests

from controller.jarvis.block import ErrorLog
from controller.jarvis.decorator import jarvis_error_handler


class JarvisWebhook:

    @staticmethod
    @jarvis_error_handler
    def error_log_hook(
        app_name: str,
        environment: str,
        target_url: Optional[str] = None,
        endpoint: Optional[str] = None,
        status_code: Optional[int] = None,
        payload: Optional[str] = None,
        description: Optional[str] = None,
    ):
        if not target_url:
            return
        response = requests.post(
            target_url,
            json=ErrorLog(
                app_name=f'{app_name} [{environment}]',
                endpoint=endpoint,
                status_code=status_code,
                payload=payload,
                description=description,
            ).block
        )
        return response
