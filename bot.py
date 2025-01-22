import asyncio

from aiogram import Bot,F,Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message,CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton

token = '<KEY>'
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())




def main():
    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    main()