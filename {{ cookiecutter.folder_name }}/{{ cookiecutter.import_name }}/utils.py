"""
Script for small utility functions used in {{ cookiecutter.repo_name }}
"""
############
# Standard #
############
import os
import inspect
import logging
import logging.config
from pathlib import Path
from logging.handlers import RotatingFileHandler

###############
# Third Party #
###############
import yaml
import coloredlogs

logger = logging.getLogger(__name__)

class RotatingFileHandlerRelativePath(logging.handlers.RotatingFileHandler):
    """
    Extension of the filehandler class that appends the current directory to the
    inputted filename. This is so the log files can be found relative to this 
    file rather than from wherever the script is run.
    """
    def __init__(self, filename, *args, **kwargs):
        filename_full = os.path.join(os.path.dirname(__file__), filename)
        super().__init__(filename_full, *args, **kwargs)


def absolute_submodule_path(submodule, cur_dir=inspect.stack()[0][1]):
    """
    Returns the absolute path of the inputted {{ cookiecutter.repo_name }} submodule 
    based on an inputtet absolute path, or the absolute path of this file.

    Parameters
    ----------
    submodule : str or Path
        Desired submodule path.

    cur_dir : str or Path, optional
        Absolute path to use as a template for the full submodule path.

    Returns
    -------
    full_path : str
        Full string path to the inputted submodule.
    """
    dir_parts = Path(cur_dir).parts
    sub_parts = Path(submodule).parts
    base_path = Path(*dir_parts[:dir_parts.index(sub_parts[0])])
    if str(base_path) == ".":
        logger.warning("Could not match base path with desired submodule.")
    full_path = base_path / Path(submodule)
    return str(full_path)

DIR_MODULE = Path(absolute_submodule_path("{{ cookiecutter.repo_name }}/"))
DIR_LOGS = DIR_MODULE / "logs"

def setup_logging(path_yaml=None, dir_logs=None, default_level=logging.INFO):
    """
    Sets up the logging module to make a properly configured logger.

    This will go into the ``logging.yml`` file in the top level directory, and
    try to load the logging configuration. If it fails for any reason, it will
    just use the default configuration. For more details on how the logger will
    be configured, see the ``logging.yml`` file.

    Parameters
    ----------
    path_yaml : str or Path, optional
        Path to the yaml file.

    dir_logs : str or Path, optional
        Path to the log directory.
        
    default_level : logging.LEVEL, optional
        Logging level for the default logging setup if the yaml fails.
    """
    # Get the yaml path
    if path_yaml is None:
        path_yaml = DIR_MODULE / "logging.yml"
    # Make sure we are using Path objects
    else: 
        path_yaml = Path(path_yaml)
    # Get the log directory
    if dir_logs is None:
        dir_logs = DIR_LOGS
    # Make sure we are using Path objects
    else:
        dir_logs = Path(dir_logs)
        
    # Make the log directory if it doesn't exist
    if not dir_logs.exists(): 
        dir_logs.mkdir()

    log_files = ['info.log', 'errors.log', 'debug.log',  'critical.log', 
                 'warn.log']
    for log_file in log_files:
        path_log_file = dir_logs / log_file
        # Make the log files if they don't exist
        if not path_log_file.exists():
            path_log_file.touch()
        # Set permissions to be accessible to everyone
        if path_log_file.stat().st_mode != 33279:
            path_log_file.chmod(0o777)        

    # Set up everything if the yaml file is present
    if path_yaml.exists():
        with open(path_yaml, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
                logging.error(e)
                coloredlogs.install(level=default_level)

    # Just use the normal configuration
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')
