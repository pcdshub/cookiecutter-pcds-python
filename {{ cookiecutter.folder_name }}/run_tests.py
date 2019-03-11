#!/usr/bin/env python

import os
import sys
import pytest
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


if __name__ == '__main__':
    # Show output results from every test function
    # Show the message output for skipped and expected failures
    args = ['-vrxs']

    # Add extra arguments
    if len(sys.argv) > 1:
        args.extend(sys.argv[1:])

    print('pytest arguments: {}'.format(args))

    # Setup logger and log everything to a file
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    log_dir = Path(os.path.dirname(__file__)) / 'logs'
    log_file = log_dir / 'run_tests_log.txt'

    if not log_dir.exists():
        log_dir.mkdir(parents=True)
        # Create the file if it doesnt already exist
    if not log_file.exists():
        log_file.touch()

    handler = RotatingFileHandler(str(log_file), backupCount=5,
                                  maxBytes=1024*1024*10, encoding=None,
                                  delay=0)
    formatter = logging.Formatter(fmt=('%(asctime)s.%(msecs)03d '
                                       '%(module)-10s '
                                       '%(levelname)-8s '
                                       '%(threadName)-10s '
                                       '%(message)s'),
                                  datefmt='%H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    logger = logging.getLogger(__name__)
    logger.info('pytest arguments: {}'.format(args))

    sys.exit(pytest.main(args))
