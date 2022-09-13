import logging
import pathlib
from pathlib import Path
import sys
from datetime import datetime
from logging import handlers
import toml

path = pathlib.Path(__file__).parent.absolute()
configfile = path / 'config.toml'
config = toml.load(configfile)

LEVEL_LIST = ['NONSET', 'INFO', 'DEBUG', 'ERROR', 'WARNING']

def configLogger(name, filename=None, config=None, default_lv=str, console_lv=str, file_lv=str):

    # Checking Level
    if default_lv and default_lv in LEVEL_LIST:
        default_lv = default_lv
    else:
        default_lv = 'NONSET'
    
    if console_lv and console_lv in LEVEL_LIST:
        console_lv = console_lv
    else:
        console_lv = 'NONSET'
    
    if file_lv and file_lv in LEVEL_LIST:
        file_lv = file_lv
    else:
        file_lv = 'NONSET'

    logging.getLogger().setLevel(level=default_lv)
    logging.getLogger("filelock").setLevel(logging.ERROR) ## Avoid lockfile log

    if filename:
    # Add stdout handler, with level INFO
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(level=console_lv)
        formatter = logging.Formatter('PID: %(process)d - ThreadID: %(thread)d - Time: %(asctime)s - Level: %(levelname)s - Function: %(funcName)s - Message: %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)

        path = Path(filename).parent.absolute()
        rawlog_path = path / "log"
        rawlog_path.mkdir(parents=True, exist_ok=True)
        logName = Path(filename).stem
        logNameWithExtension = Path(filename).stem + '.log'
        logFileFullPath = rawlog_path / logNameWithExtension

        # logFileFullPath = rawlog_path / logFormat
        file_handler = handlers.TimedRotatingFileHandler(logFileFullPath, when='midnight', backupCount=0, encoding='utf-8')
        file_handler.suffix = "%Y-%m-%d.log"

        # file_handler = logging.FileHandler(logFileFullPath, encoding='utf-8')
        file_handler.setLevel(level=file_lv)
        file_handler.setFormatter(formatter)
        logging.getLogger().addHandler(file_handler)
        log = logging.getLogger("app." + logName)
    else:
        log = logging.getLogger("app." + name)

    # log.debug('Debug message, should only appear in the file.')
    # log.info('Info message, should appear in file and stdout.')
    # log.warning('Warning message, should appear in file and stdout.')
    # log.error('Error message, should appear in file and stdout.')
    return log
