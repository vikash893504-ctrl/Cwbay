from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_command(bot: Client, message: Message):
    await message.reply_text(
        f"Hello {message.from_user.mention},\n\n"
        "Bot active hai aur sahi kaam kar raha hai!"
    )

@Client.on_message(filters.command("help") & filters.private)
async def help_command(bot: Client, message: Message):
    await message.reply_text("Kuch madad chahiye?")
  
