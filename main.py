from aiogram import Bot, Dispatcher
from core.handlers.basic import get_command, send_message_cron
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command
from core.utils.commands import set_commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот выключен!")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_command, Command('start', 'stop', 'anekdot', 'timer'))
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message_cron, 'interval', hours=4, kwargs={'bot': bot})
    scheduler.start()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
