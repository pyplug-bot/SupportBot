from aiogram import Bot
from aiogram.types import User
from config import CHANNEL_USERNAME, GROUP_USERNAME


async def check_membership(bot: Bot, user: User):

    chats = [
        CHANNEL_USERNAME,
        GROUP_USERNAME
    ]

    for chat in chats:
        try:
            member = await bot.get_chat_member(
                chat_id=chat,
                user_id=user.id
            )

            if member.status in ["left", "kicked"]:
                return False

        except Exception:
            return False

    return True