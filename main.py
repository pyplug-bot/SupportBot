import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import create_tables

from handlers.start import router as start_router
from handlers.request import router as request_router
from handlers.admin import router as admin_router


async def main():
    # Create database tables
    create_tables()

    # Create bot
    bot = Bot(token=BOT_TOKEN)

    # Create dispatcher
    dp = Dispatcher()

    # Register routers
    dp.include_router(start_router)
    dp.include_router(request_router)
    dp.include_router(admin_router)

    print("✅ Support Bot Started Successfully")

    # Start bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())