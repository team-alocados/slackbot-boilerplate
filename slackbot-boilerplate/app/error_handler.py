from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from jose import JWTError

from app.response import (
    bad_jwt_token, bad_request, forbidden, not_found, unprocessable_entity,
)
from controller.jarvis import JarvisWebhook


def init_app(app: FastAPI):

    @app.exception_handler(400)
    async def bad_request_handler(
        request: Request,
        exc: HTTPException
    ):
        return bad_request(exc.detail)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):
        """Validation Exception Handler"""
        errors: list = exc.errors()
        detail = errors[0].get('msg') if errors else None
        for e in errors:
            if e.get('ctx'):
                e['ctx'] = str(e['ctx'])
        
        return unprocessable_entity(detail, errors)

    @app.exception_handler(JWTError)
    async def unauthorized_handler(
        request: Request,
        exc: JWTError
    ):
        return bad_jwt_token(str(exc.args[0]))

    @app.exception_handler(403)
    async def not_found_handler(
        request: Request,
        exc: HTTPException
    ):
        return forbidden(detail=exc.detail)

    @app.exception_handler(404)
    async def not_found_handler(
        request: Request,
        exc: HTTPException
    ):
        return not_found

    @app.exception_handler(500)
    async def internal_server_error_handler(
        request: Request,
        exc: HTTPException
    ):
        JarvisWebhook.error_log_hook(
            app_name=request.app.settings.app_name,
            environment=request.app.settings.environment,
            target_url=request.app.settings.error_log_webhook,
            endpoint=request.url.path,
            status_code=500,
            payload=exc.args[0]
        )
        return ORJSONResponse(
            {'msg': 'internal_server_error'},
            status_code=500,
        )
