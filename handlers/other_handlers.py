from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import LEXICON

#Инициализация роутера уровня модуля
router = Router()


#Хэндлер, который запускает поиск одежды
@router.message(F.text.replace(' ', '').isalpha())
async def send_answer(message: Message):
    cloth = message.text
    await message.answer(text=LEXICON['answer'])


#Запуск новых настроек
@router.message(F.text == LEXICON['button1'])
async def send_settings(message: Message):
    await message.answer(text='Что-то тут явно будет')


#Этот хэндлер будет срабатывать на все другие сообщения
@router.message()
async def send_error(message: Message):
    await message.reply(LEXICON['error'])