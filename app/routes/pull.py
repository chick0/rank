from flask import Blueprint
from pydantic import BaseModel

from app.models import Rank

bp = Blueprint("pull", __name__, url_prefix="/api/pull")


class RankResponse(BaseModel):
    id: int
    name: str
    score: int
    created_at: int


class RankList(BaseModel):
    list: list[RankResponse]


@bp.get("")
def pull():
    return RankList(
        list=[
            RankResponse(
                id=x.id,
                name=x.name,
                score=x.score,
                created_at=int(x.created_at.timestamp())
            )
            for x in Rank.query.order_by(
                Rank.score.desc()
            ).filter(
                Rank.score > 0
            ).limit(50).all()
        ]
    ).dict()
