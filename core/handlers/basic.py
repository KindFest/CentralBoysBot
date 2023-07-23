import asyncio
from aiogram import Bot
from aiogram.types import Message
from core.utils.utils import datebase, get_anekdot
import json


async def send_message_cron(bot: Bot):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        if data[item].get('anekdot'):
            if data[item]['anekdot']['is_timer_active'] and data[item]['anekdot']['is_chat_active']:
                await bot.send_message(data[item]['anekdot']['chat_id'], get_anekdot())


async def delete_message(message_lst):
    await asyncio.sleep(3)
    for message in message_lst:
        await message.delete()


async def get_command(message: Message, bot: Bot):
    msg = await message.answer(datebase(message.text, message.chat.id))
    if '/anekdot' in message.text and 'Сначала нужно активировать бота командой /start' != msg.text:
        await delete_message([message])
    else:
        await delete_message([message, msg])
