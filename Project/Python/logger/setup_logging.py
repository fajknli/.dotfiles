#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2026-03-25 13:02


import logging
import sys

def setup_logging(log_file="app.log", verbose=False):
    level = logging.DEBUG if verbose else logging.INFO

    logger = logging.getLogger("RAG")
    logger.setLevel(level)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    print("调试:"logger.handlers)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


    print("调试:"logger.handlers)

    return logger

log = setup_logging(verbose=True)

log.debug("错误信息")
log.info("普通信息")
log.warning("警告信息")
log.error("错误信息")
log.critical("严重信息")
