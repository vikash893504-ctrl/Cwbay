from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config

# Safe Auth User Checking
def is_auth_user(user_id):
    try:
        if isinstance(Config.AUTH_USERS, str):
            auth_list = [int(x.strip()) for x in Config.AUTH_USERS.split(",") if x.strip()]
        elif isinstance(Config.AUTH_USERS, list):
            auth_list = Config.AUTH_USERS
        else:
            auth_list = [8211049757]
        return user_id in auth_list
    except Exception:
        return True

@Client.on_message(filters.command("start"))
async def start_handler(bot: Client, message: Message):
    user_id = message.from_user.id
    
    if not is_auth_user(user_id):
        await message.reply_text("❌ Aap is bot ko use karne ke liye authorized nahi hain.")
        return

    await message.reply_text(
        "👋 **Welcome Boss!**\n\n"
        "StarkBot bilkul active hai aur aapke sare plugins (`cp.py`, `pw.py`, `khan.py` etc.) working state me hain.\n\n"
        "Kisi bhi plugin ka command bhej kar test karein!"
    )
  
