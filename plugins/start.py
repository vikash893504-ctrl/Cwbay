from pyrogram import Client, filters
from pyrogram.types import Message

# Har tarah ke private message par reply karega (Command ho ya na ho)
@Client.on_message(filters.private)
async def catch_all(bot: Client, message: Message):
    print(f"MESSAGE RECEIVED: {message.text}")
    await message.reply_text(f"Received: {message.text}")
  
