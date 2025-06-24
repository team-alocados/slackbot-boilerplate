from fastapi import Depends, HTTPException, Request
from slack_sdk.signature import SignatureVerifier

from app.depends.module import app_slack_verifier


async def verify_request(
    request: Request,
    slack_verifier: SignatureVerifier = Depends(app_slack_verifier)
):
    body = await request.body()
    headers = request.headers
    if not slack_verifier.is_valid_request(body=body, headers=headers):
        raise HTTPException(403, "Invalid slack request signature")
    return
