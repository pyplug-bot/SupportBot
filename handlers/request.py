from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline import account_status_keyboard, reason_keyboard

router = Router()


@router.callback_query(F.data == "continue")
async def continue_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "📌 Select your account status:",
        reply_markup=account_status_keyboard()
    )


@router.callback_query(F.data.startswith("status_"))
async def status_handler(callback: CallbackQuery):

    status = callback.data.replace("status_", "")

    await callback.message.edit_text(
        f"Got it!\n\n"
        f"Your account status: {status.title()}\n\n"
        "Now select the reason:",
        reply_markup=reason_keyboard()
    )


@router.callback_query(F.data.startswith("reason_"))
async def reason_handler(callback: CallbackQuery):

    reason = callback.data.replace("reason_", "")

    await callback.message.edit_text(
        f"✅ Got it!\n\n"
        f"Account status: Selected\n"
        f"Reason: {reason.replace('_', ' ').title()}\n\n"
        "Please send your Instagram username."
    )