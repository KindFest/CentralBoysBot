from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы Бота'
        ),
        BotCommand(
            command='stop',
            description='Завершить работу БОТа'
        ),
        BotCommand(
            command='anekdot',
            description='Получить случайный анекдот'
        ),
        BotCommand(
            command='timer',
            description='Активация таймера, выдача случайного анекдота 1 раз в 4 часа'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
