from os.path import join

from flask import Blueprint
from flask import request
from pydantic import BaseModel

from app import BASE_DIR
from app import db
from app.models import Rank

bp = Blueprint("drop", __name__, url_prefix="/api/drop")


class DropRequest(BaseModel):
    id: int
    code: str


class DropResponse(BaseModel):
    result: bool
    message: str


def get_code() -> str:
    try:
        with open(join(BASE_DIR, "code.txt"), mode="r") as code_reader:
            return code_reader.read().strip()
    except FileNotFoundError:
        return "chick0/rank"


@bp.post("")
def drop():
    ctx = DropRequest(**request.json)

    if ctx.code != get_code():
        return DropResponse(
            result=False,
            message="비밀번호가 일치하지 않습니다."
        ).dict(), 403

    rn = Rank.query.filter_by(
        id=ctx.id
    ).delete()

    if rn == 0:
        return DropResponse(
            result=False,
            message="등록된 랭킹이 아닙니다."
        ).dict(), 400

    db.session.commit()

    return DropResponse(
        result=True,
        message="삭제되었습니다."
    ).dict()
