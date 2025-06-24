from fastapi import Request
from settings import Settings
from slack_sdk.signature import SignatureVerifier


def app_settings(request: Request) -> Settings:
    """Nepto Settings Controller"""
    return request.app.settings

def app_slack_verifier(request: Request) -> SignatureVerifier:
    """Slack Verifier Controller"""
    return request.app.slack_verifier
