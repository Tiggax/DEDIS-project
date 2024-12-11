from split_settings.tools import include
import logging
logger = logging.getLogger(__name__)

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

from os import environ



cfg = environ

DEBUG = "DEBUG" in dotenv_values()

include("default.py", scope = globals())

if os.environ.get("ENV_TYPE") in ['Production', "prod", "Prod"]:
    include("prod.py", scope = globals())
else:
    include("dev.py", scope = globals())