from fastapi import APIRouter


slack = APIRouter()

from . import action
from . import command
from . import event
from . import oauth
