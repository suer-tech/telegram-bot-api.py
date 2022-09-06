from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

import BinApi
import invest
from config import TOKEN
from keyboard import greet_kb1

import importlib

from datetime import datetime

import asyncio

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

current_datetime = datetime.now()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDZ2JEZuGR8N1D5s__y0O8cIUGMk9OAAIiEwACXWxwS64th70744A-IwQ')
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=greet_kb1)

@dp.message_handler(Text(equals="ТОП +"))
async def with_puree(message: types.Message):
    from BinApi import topplus
    await bot.send_message(message.chat.id,topplus)
    importlib.reload(BinApi)

@dp.message_handler(Text(equals="ТОП -"))
async def with_puree(message: types.Message):
    from BinApi import topminus
    await bot.send_message(message.chat.id, topminus)
    importlib.reload(BinApi)

@dp.message_handler(Text(equals="Индексы и сырье"))
async def with_puree(message: types.Message):
    from invest import index
    mess = index
    await bot.send_message(message.chat.id, mess, parse_mode='html', disable_web_page_preview = True)
    importlib.reload(invest)


if __name__ == '__main__':
    executor.start_polling(dp)

