import logging
from os import getenv

# Database settings
DB_HOST = "mongodb://mongodb:27017"
DB_NAME = "ApplicationDatabase"

# Logging settings
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"

# Bot settings
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_ADMIN_USERNAMES = [
    username.strip()
    for username in getenv("BOT_ADMIN_USERNAMES", default="").split(",")
    if username.strip()
]
