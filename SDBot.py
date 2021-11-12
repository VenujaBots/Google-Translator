from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "2121977275:AAHGkOfO62Py7g6Salx8v4BrBR8Ay2WXhyE")

API_ID = int(os.environ.get("API_ID",7395896))

API_HASH = os.environ.get("API_HASH", "cd3998ddf318dad74d7c506731bc0abc")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "GTBot",
        bot_token=TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    app.run()

