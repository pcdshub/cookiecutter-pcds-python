#!/usr/bin/env python
############
# Standard #
############
import os
import sys
import pytest
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler
import shutil

###############
# Third Party #
###############
from cookiecutter import main

if __name__ == '__main__':
    # Show output results from every test function
    # Show the message output for skipped and expected failures
    args = ['-v', '-vrxs', '--ignore={{ cookiecutter.repo_name }}']

    # Add extra arguments
    if len(sys.argv) >1:
        args.extend(sys.argv[1:])

    # Setup logger and log everything to a file
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    log_dir = Path(os.path.dirname(__file__)) / 'logs'
    log_file = log_dir / 'run_tests.log'

    if not log_dir.exists():
        log_dir.mkdir(parents=True)
        # Create the file if it doesnt already exist
    if not log_file.exists():
        log_file.touch()
        
    handler = RotatingFileHandler(str(log_file), backupCount=5,
                                  maxBytes=1024*1024*10, encoding=None, delay=0)
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
    
    # Decide if we are running tests on the cookiecutter
    if '--no-template' in args:
        args.remove('--no-template')
        args.append('--ignore=tests')
        
    # Run the tests in the project
    out_dir = Path('data-project')
    if '--no-project' in args:
        args.remove('--no-project')
    else:
        CCDS_ROOT = os.path.abspath(os.path.join(__file__, os.pardir))
        main.cookiecutter(CCDS_ROOT, no_input=True, extra_context={},
                          output_dir=str(out_dir))

    # Run the tests
    try:
        sys.exit(pytest.main(args))
    finally:
        # Cleanup the created project if it exists
        if out_dir.exists(): shutil.rmtree(str(out_dir))
