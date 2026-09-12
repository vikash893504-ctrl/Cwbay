#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>

import os
import sys

# System Path Fix (ताकि config और cw.py ढूँढने में error न आए)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

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

# Auth Users
AUTH_USERS = [ int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

if __name__ == "__main__" :
    bot = Client(
        "StarkBot",
        bot_token="8685753606:AAE3cS4-TAsS_eIjVM50NM0qnq4vhTAtrtc",
        api_id=34435812,
        api_hash="ec83fcc94203532d52146a458cc9a274",
        sleep_threshold=20,
        plugins=plugins,
        workers=50
    )
    
    async def main():
        await bot.start()
        bot_info  = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()
    
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped-->")
  
