from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID

router = Router()


@router.message(Command("panel"))
async def panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        """
🛠 ADMIN PANEL

/panel - Open Panel
/stats - Bot Statistics
/broadcast - Broadcast Message

Bot Status: 🟢 Online
        """
    )


@router.message(Command("stats"))
async def stats(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        """
📊 BOT STATS

👥 Users: Coming Soon
📩 Requests: Coming Soon

✅ Database Connected
        """
    )