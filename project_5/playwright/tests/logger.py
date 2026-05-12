# -*- coding: utf-8 -*-
"""Console logging setup for Playwright demo scripts (uses stdlib ``logging``)."""

import logging
import sys

_LOGGER_NAME = "saucedemo"


def get_logger(name: str = _LOGGER_NAME) -> logging.Logger:
    """Return a logger that prints plain messages to stdout (one line per call)."""
    log = logging.getLogger(name)
    if log.handlers:
        return log
    log.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(message)s"))
    log.addHandler(handler)
    log.propagate = False
    return log
