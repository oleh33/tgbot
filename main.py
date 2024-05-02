import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message 

bot = Bot(token='6852106360:AAEcnIBBdYr9hJO8X6doxnCP5GfxPGOi420')
dp = Dispatcher()


@dp.message_handler()
async def cmd_start(message: Message):
    await message.answer('Привіт, що тебе цікавить!')



async def main():
    awaint .start_polling(bot)


if name == 'main': 
    asyncio.run(main()) 
from aiogram import Bot, Dispatcher
from aiogram.types import Message 

bot = Bot(token='6852106360:AAEcnIBBdYr9hJO8X6doxnCP5GfxPGOi420')
dp = Dispatcher()


@dp.message_handler()
async def cmd_start(message: Message):
    await message.answer('Привіт, що тебе цікавить!')



async def main():
    awaint .start_polling(bot)


if name == 'main': 
    asyncio.run(main())