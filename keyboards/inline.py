from aiogram.utils.keyboard import InlineKeyboardBuilder


def account_status_keyboard():

    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="🔴 Disabled",
        callback_data="status_disabled"
    )

    keyboard.button(
        text="🟠 Suspended",
        callback_data="status_suspended"
    )

    keyboard.adjust(1)

    return keyboard.as_markup()


def reason_keyboard():

    keyboard = InlineKeyboardBuilder()

    reasons = [
        ("Integrity", "reason_integrity"),
        ("Fraud & Deception", "reason_fraud"),
        ("Privacy & Security", "reason_privacy"),
        ("Child Safety", "reason_child"),
        ("Copyright (CPR)", "reason_cpr"),
        ("DNR", "reason_dnr"),
        ("Other", "reason_other")
    ]

    for text, data in reasons:
        keyboard.button(
            text=text,
            callback_data=data
        )

    keyboard.adjust(1)

    return keyboard.as_markup()