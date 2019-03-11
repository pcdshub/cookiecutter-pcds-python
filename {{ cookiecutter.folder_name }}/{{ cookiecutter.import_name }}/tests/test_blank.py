"""
This document and its single test are included only so that first-time builds
with doctr will succeed and create an empty document.
"""
import logging


logger = logging.getLogger(__name__)


def test_blank():
    raise ZeroDivisionError()
