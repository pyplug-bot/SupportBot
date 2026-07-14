from aiogram.fsm.state import StatesGroup, State


class AccountForm(StatesGroup):
    username = State()
    screenshot = State()
    email = State()