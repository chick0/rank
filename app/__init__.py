from os.path import join
from os.path import abspath
from os.path import dirname
from importlib import import_module

from flask import Flask
from flask import Response
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import NotFound

BASE_DIR = dirname(dirname(abspath(__file__)))
DIST_DIR = join(BASE_DIR, "dist")

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder=None)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR}/rank.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    import_module("app.models")
    db.init_app(app)
    migrate.init_app(app, db)

    @app.get("/")
    @app.get("/<path:path>")
    def frontend(path = None):  # noqa: E251
        if path is None:
            return "지정된 경로가 없습니다.", 400

        try:
            response: Response = send_from_directory(
                directory=DIST_DIR,
                path=path
            )
        except NotFound:
            return "파일을 찾을수 없습니다.", 404

        if path.endswith(".js"):
            response.content_type = "text/javascript; charset=utf-8"

        return response

    from app.routes import pull
    from app.routes import push
    app.register_blueprint(pull.bp)
    app.register_blueprint(push.bp)

    return app
