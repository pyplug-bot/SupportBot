import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
GROUP_USERNAME = os.getenv("GROUP_USERNAME")