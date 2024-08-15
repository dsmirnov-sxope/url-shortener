"""
Configuration module for shortener.
"""

import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def get_config_path() -> Path:
    """
    Get configuration file's path from the environment variable.

    Returns:
        Path: path of the configuration file
    """
    prefix = os.getenv("PATH_PREFIX", ".")
    config = os.getenv("SERVICE_CONFIG_PATH", "config/config.yml")
    return Path(prefix) / Path(config)
