# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

# Load config.env for local development (optional - not required for Railway)
# Railway deployments use environment variables set in Railway dashboard
try:
    load_dotenv("config.env")
except:
    pass

# Validate BOT_TOKEN from environment variable (works with both local config.env and Railway env vars)
if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count(":") == 1:
    print("Error: BOT_TOKEN environment variable must be set in format '123456:abcdefghijklmnopqrstuvwxyz'")
    print("For local dev: Set BOT_TOKEN in config.env file")
    print("For Railway: Set BOT_TOKEN environment variable in Railway dashboard")
    exit(1)

# Validate SESSION_STRING from environment variable (works with both local config.env and Railway env vars)
if (
    not getenv("SESSION_STRING")
    or getenv("SESSION_STRING") == "xxxxxxxxxxxxxxxxxxxxxxx"
):
    print("Error: SESSION_STRING environment variable must be set with a valid string")
    print("For local dev: Set SESSION_STRING in config.env file")
    print("For Railway: Set SESSION_STRING environment variable in Railway dashboard")
    exit(1)


# Pyrogram configuration
# All values read from environment variables (works with config.env for local dev or Railway env vars)
class PyroConf(object):
    API_ID = int(getenv("API_ID", "6"))
    API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = getenv("BOT_TOKEN")
    SESSION_STRING = getenv("SESSION_STRING")
    BOT_START_TIME = time()

    # Optional performance settings (can be overridden via environment variables)
    MAX_CONCURRENT_DOWNLOADS = int(getenv("MAX_CONCURRENT_DOWNLOADS", "3"))
    BATCH_SIZE = int(getenv("BATCH_SIZE", "10"))
    FLOOD_WAIT_DELAY = int(getenv("FLOOD_WAIT_DELAY", "3"))
