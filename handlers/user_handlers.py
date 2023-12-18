from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram import Router
from lexicon.lexicon import LEXICON
from aiogram.utils.keyboard import ReplyKeyboardBuilder

#Инициализация роутера уровня модуля
router = Router()

#Инициализация билдера и передача в него кнопки
kb_builder = ReplyKeyboardBuilder()
kb_builder.row(KeyboardButton(text=LEXICON['button1']))


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON['/start'],
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])
