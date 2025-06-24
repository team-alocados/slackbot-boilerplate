from functools import wraps

from loguru import logger


def jarvis_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response is None:
            return
        if response.status_code == 400:
            kwargs['payload'] = "페이로드 호출에 실패했습니다. Raw Log를 참고해주세요."
            response = func(*args, **kwargs)
        if response.status_code != 200:
            logger.error(f"Jarvis API 전송 실패: ({response.status_code}, {response.text})")
        return response
    return wrapper
