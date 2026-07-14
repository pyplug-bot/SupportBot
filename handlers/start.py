from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.forcejoin import check_membership

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):

    joined = await check_membership(
        message.bot,
        message.from_user
    )

    if not joined:

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
            text="✅ Check Again",
            callback_data="check_join"
        )

        keyboard.adjust(1)

        await message.answer(
            "⚠️ Please join our Channel and Group first.",
            reply_markup=keyboard.as_markup()
        )
        return


    username = message.from_user.username

    name = f"@{username}" if username else message.from_user.first_name


    await message.answer(
        f"👋 Welcome {name}\n\n"
        "Select your account status to continue."
    )