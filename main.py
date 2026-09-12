import asyncio
from pyrogram import Client, idle
from config import Config
from web import run

# Client setup
app = Client(
    "StarkBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def main():
    await app.start()
    print("<--- Bot Started Successfully --->")
    await idle()
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
  
