import asyncio

from aiogram import Bot,F,Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message,CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton

token = '7874928619:AAHdmduqLLfYUQF-Tgw_aXYcMp41X3maLTc'
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)


def main():
    asyncio.run(dp.start_polling(bot,skip_updates=True))


if __name__ == '__main__':
    try:
        print('waiting...')
        main()
    except KeyboardInterrupt:
        print('Goodbye!')