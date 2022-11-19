from datetime import datetime

from flask import Blueprint
from flask import request
from pydantic import BaseModel

from app import db
from app.models import Rank

bp = Blueprint("push", __name__, url_prefix="/api/push")


class RankRequest(BaseModel):
    name: str
    score: int


@bp.post("")
def push():
    ctx = RankRequest(**request.json)

    rank = Rank()
    rank.name = ctx.name
    rank.score = ctx.score
    rank.created_at = datetime.now()

    db.session.add(rank)
    db.session.commit()

    return {}, 201
