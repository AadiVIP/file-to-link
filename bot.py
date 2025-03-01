from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("file_to_link_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.document)
async def file_to_link(client, message):
    file = message.document or message.video or message.audio
    if not file:
        return await message.reply_text("Please send a valid file.")
    
    file_link = f"https://t.me/{client.me.username}?start={message.id}"
    await message.reply_text(f"✅ Your download link:\n🔗 {file_link}")

if __name__ == "__main__":
    app.run()
