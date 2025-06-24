import json
from urllib.parse import parse_qs

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

    return body


async def action_verify_request(
    body: bytes = Depends(verify_request)
):
    form_dict = parse_qs(body.decode())
    # parse_qs 결과는 항상 리스트로 감싸져 있음
    if "payload" not in form_dict:
        raise HTTPException(400, "Missing payload")

    try:
        payload = json.loads(form_dict["payload"][0])
    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid payload format")
    return payload


async def command_verify_request(
    body: bytes = Depends(verify_request)
):
    form_dict = parse_qs(body.decode())
    return {
        "team_id": form_dict["team_id"][0],
        "channel_id": form_dict["channel_id"][0],
        "channel_name":  form_dict["channel_name"][0],
        "user_id": form_dict["user_id"][0],
        "command": form_dict["command"][0],
        "is_enterprise_install": form_dict["is_enterprise_install"][0],
        "response_url": form_dict["response_url"][0],
        "trigger_id": form_dict["trigger_id"][0]
    }
