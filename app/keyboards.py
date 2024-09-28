from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_tasks

language_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Русский 🇷🇺')],
    [KeyboardButton(text='Deutsch 🇩🇪')],
    [KeyboardButton(text='English 🇬🇧')],
], resize_keyboard=True)

def actions(lang):

    match(lang):
        case 'Русский 🇷🇺':
            text='Добавить заметку.  🗒'
        case 'Deutsch 🇩🇪':
            text='Notiz hinzufügen.  🗒'
        case 'English 🇬🇧':
            text='Add note.  🗒'

    return ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=text)]
    ], resize_keyboard=True, one_time_keyboard=True)


async def tasks(tg_id):
    tasks = await get_tasks(tg_id)
    keyboard = InlineKeyboardBuilder()
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text=task.task, callback_data=f'task_{task.id}'))
    return keyboard.adjust(2).as_markup()