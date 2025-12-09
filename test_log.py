import os
import logging
import shutil
from logs import init_log

# Tests para funciones del fichero log
def test_init_log_is_a_logger():
    logger = init_log()

    assert isinstance(logger, logging.Logger)