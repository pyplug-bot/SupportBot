from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards.inline import account_status_keyboard, reason_keyboard
from states.form import AccountForm

router = Router()


@router.callback_query(F.data == "continue")
async def continue_handler(callback: CallbackQuery):

    await callback.message.edit_text(
        "📌 Select your account status:",
        reply_markup=account_status_keyboard()
    )


@router.callback_query(F.data.startswith("status_"))
async def status_handler(callback: CallbackQuery, state: FSMContext):

    status = callback.data.replace("status_", "")

    await state.update_data(status=status)

    await callback.message.edit_text(
        f"Got it!\n\n"
        f"Account status: {status.title()}\n\n"
        "Now select the reason:",
        reply_markup=reason_keyboard()
    )


@router.callback_query(F.data.startswith("reason_"))
async def reason_handler(callback: CallbackQuery, state: FSMContext):

    reason = callback.data.replace("reason_", "")

    await state.update_data(reason=reason)

    await callback.message.edit_text(
        "✅ Got it!\n\n"
        "Please send your Instagram username."
    )

    await state.set_state(AccountForm.username)


@router.message(AccountForm.username)
async def username_handler(message: Message, state: FSMContext):

    await state.update_data(
        instagram_username=message.text
    )

    await message.answer(
        "📷 Please send your screenshot:\n\n"
        "• Suspension screenshot\n"
        "• Read More page\n"
        "• Login page"
    )

    await state.set_state(AccountForm.screenshot)