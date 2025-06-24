from contextlib import asynccontextmanager

from fastapi import FastAPI
# Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import ORJSONResponse
from slack_sdk.signature import SignatureVerifier

from app import api, error_handler, middleware
# Routers
from app.api.slack import slack
from app.api.template import api as template
from app.api.v1 import api as api_v1
from settings import Settings, __VERSION__


def create_app(settings: Settings) -> FastAPI:
    """Application Factory"""

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Do something before the application starts
        yield
        # Do something after the application terminates

    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=__VERSION__,
        terms_of_service=settings.term_of_service,
        contact={
            "name": settings.contact_name,
            "url": settings.contact_url,
            "email": settings.contact_email
        },
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        default_response_class=ORJSONResponse,
        lifespan=lifespan
    )

    # App Module init
    app.settings = settings
    app.slack_verifier = SignatureVerifier(
        signing_secret=settings.slack_signing_secret
    )

    # Built-in init
    middleware.init_app(app, settings)
    error_handler.init_app(app)

    # Extension/Middleware init
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"])
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"])
    app.add_middleware(
        GZipMiddleware,
        minimum_size=1024)
    """
    # If you want to use middleware, you can add it here.
    app.add_middleware(middleware.HelloMiddleware)
    """

    # Register Routers
    app.include_router(template)
    app.include_router(api_v1, prefix='/api/v1')
    app.include_router(slack, prefix='/slack/api')

    return app
