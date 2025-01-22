import asyncio

from aiogram import Bot,F,Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton

token = '7874928619:AAHdmduqLLfYUQF-Tgw_aXYcMp41X3maLTc'
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

class Registration(StatesGroup):
    phone = State()
    home = State()

@dp.message(CommandStart())
async def start(message: Message,state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text=message.text,reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Share contact 📞',request_contact=True)]],resize_keyboard=True))
    await state.set_state(Registration.phone)

@dp.message(Registration.phone)
async def get_phone(message: Message, state: FSMContext):
    global phone
    if message.text:
        phone = message.text
    if message.contact:
        phone = message.contact.phone_number
    else:
        await message.answer(
            text='📞 **Iltimos, o`zingizning telefon raqamingizni yuboring** 😊\n\n'
                 'Agar raqamingizni jo`natgan bo`lsangiz, pastdagi tugmani bosing yoki raqamingizni qo`lda kiriting. 🔢'
        )
    await state.update_data(phone=phone)
    await state.clear()
    await state.set_state(Registration.home)


@dp.message(Registration.home)
async def home(message: Message, state: FSMContext):
    await message.answer(text='SmartFood bosh sahifasi',reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='')]]))

def main():
    asyncio.run(dp.start_polling(bot,skip_updates=True))


if __name__ == '__main__':
    try:
        print('waiting...')
        main()
    except KeyboardInterrupt:
        print('Goodbye!')