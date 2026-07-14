from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    username = message.from_user.username

    if username:
        name = f"@{username}"
    else:
        name = message.from_user.first_name

    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="📢 Join Channel",
        url="https://t.me/yourchannel"
    )

    keyboard.button(
        text="💬 Join Group",
        url="https://t.me/yourgroup"
    )

    keyboard.button(
        text="✅ Continue",
        callback_data="continue"
    )

    keyboard.adjust(1)

    await message.answer(
        f"👋 Welcome {name}\n\n"
        "Please join our Channel and Group to continue.",
        reply_markup=keyboard.as_markup()
    )