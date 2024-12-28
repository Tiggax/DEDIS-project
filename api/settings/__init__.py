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
include("hasher_settings.py", scope = globals())

ENV_TYPE = os.environ.get("ENV_TYPE")

print(f"Environment: {ENV_TYPE}")

if ENV_TYPE in ['production', 'Production', "prod", "Prod"]:
    include("prod.py", scope = globals())
else:
    include("dev.py", scope = globals())