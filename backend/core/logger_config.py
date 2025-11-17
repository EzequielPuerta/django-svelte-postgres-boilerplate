import logging
import sys
from logging import LogRecord
from pathlib import Path

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: LogRecord) -> None:
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


def setup_logging(base_dir: Path) -> None:
    logger.remove()
    logger.add(sys.stdout, level="DEBUG", colorize=True)
    logger.add(
        base_dir / "logs/django.log",
        rotation="10 MB",
        retention="7 days",
        level="INFO",
        encoding="utf-8",
    )
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
