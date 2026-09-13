import os
import asyncio
import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client, idle
import tgcrypto
from pyromod import listen
from config import Config
from web import keep_alive

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Safe Fallback for Auth Users
try:
    if isinstance(Config.AUTH_USERS, str):
        AUTH_USERS = [int(chat.strip()) for chat in Config.AUTH_USERS.split(",") if chat.strip()]
    elif isinstance(Config.AUTH_USERS, list):
        AUTH_USERS = Config.AUTH_USERS
    else:
        AUTH_USERS = [8211049757]
except Exception:
    AUTH_USERS = [8211049757]

# Prefixes 
prefixes = ["/", "~", "?", "!"]
plugins = dict(root="plugins")

# Direct Credentials Setup to Prevent NoneType Crash
BOT_TOKEN = os.environ.get("BOT_TOKEN") or getattr(Config, "BOT_TOKEN", "8685753606:AAE3cS4-TAsS_eIjVM50NM0qnq4vhTAtrtc")
API_ID = int(os.environ.get("API_ID") or getattr(Config, "API_ID", 34435812))
API_HASH = os.environ.get("API_HASH") or getattr(Config, "API_HASH", "ec83fcc94203532d52146a458cc9a274")

if __name__ == "__main__":
    # Start Flask Web Server in background for Render
    keep_alive()

    bot = Client(
        "StarkBot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        sleep_threshold=20,
        plugins=plugins,
        workers=50
    )
    
    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()
        await bot.stop()
    
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<---Bot Stopped--->")
  
