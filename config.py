import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

ANGEL_API_KEY = os.getenv("ANGEL_API_KEY")
ANGEL_CLIENT_ID = os.getenv("ANGEL_CLIENT_ID")
ANGEL_PASSWORD = os.getenv("ANGEL_PASSWORD")
ANGEL_TOTP = os.getenv("ANGEL_TOTP")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print("TOKEN:", TELEGRAM_TOKEN)
print("CHAT:", CHAT_ID)