from sys import stdout
from logging import getLogger
from logging import StreamHandler
from logging import Formatter
from logging import INFO

from waitress import serve

from app import create_app

logger = getLogger()


def init_logger():
    logger.setLevel(INFO)
    handler = StreamHandler(stdout)
    handler.setFormatter(fmt=Formatter("%(asctime)s [%(levelname)s]: %(message)s", "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(hdlr=handler)


def start_app():
    host, port = "127.0.0.1", 21313
    serve(app=create_app(), host=host, port=port)


if __name__ == "__main__":
    init_logger()
    start_app()
