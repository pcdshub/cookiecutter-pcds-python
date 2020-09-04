import logging

logger = logging.getLogger(__name__)


def test_blank():
    raise ZeroDivisionError()
