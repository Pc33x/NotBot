from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from app.database.requests import set_user, del_task, set_task
from app.states import Start
from app.language import Language
import app.keyboards as kb

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await set_user(message.from_user.id)
    await state.set_state(Start.language)
    await message.answer('Choose language.',
                         reply_markup=kb.language_menu)


@user.message(Start.language)
async def choose_language(message: Message, state: FSMContext):
    global info
    await state.update_data(language=message.text)
    data = await state.get_data()
    info = Language(data['language']).get_data()
    await message.answer(f'{info['text_info']} {data['language']}',
                         reply_markup=kb.actions(data['language']))
    await state.clear()


@user.message(F.text.endswith('🗒'))
async def add_note(message: Message):
    await message.answer(f'{info['text_add_note']}',
                         reply_markup=await kb.tasks(message.from_user.id))


@user.callback_query(F.data.startswith('task_'))
async def delete_task(callback: CallbackQuery):
    await callback.answer(f'{info['delete_info_callback']}')
    await del_task(callback.data.split('_')[1])
    await callback.message.delete()
    await callback.message.answer(f'{info['delete_info']} ✖️\n\n{info['text_add_note']}',
                                  reply_markup=await kb.tasks(callback.from_user.id))


@user.message()
async def add_task(message: Message):
    if len(message.text) > 128:
        await message.answer(f'{info['text_long_err']}')
        return
    await set_task(message.from_user.id, message.text)
    await message.answer(f'{info['add_info']} ☑️\n\n{info['text_add_note']}',
                         reply_markup=await kb.tasks(message.from_user.id))
