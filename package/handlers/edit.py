from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from package.db import all_words

router = Router()


class EditState(StatesGroup):
    word = State()
    new_defition = State()


@router.message(Command(commands=['edit']))
async def edit_handler(message: types.Message, state: FSMContext):
    await state.set_state(EditState.word)
    await message.reply(
        'Send me the word the definition of which your would like to edit'
    )


@router.message(EditState.word)
async def edit_word_handler(message: types.Message, state: FSMContext):
    to_edit = message.text
    if to_edit is None:
        await message.reply(
            'Please, provide me with a word the definition of which you would like to edit, see the /list'
        )

        await state.clear()
        return

    if to_edit not in all_words:
        await message.reply(
            'The word you are trying to edit does not seem to be present in the dictionary, you should try to /add it or to look into the /list'
        )

        await state.clear()
        return

    await state.update_data(word=message.text)
    await state.set_state(EditState.new_defition)

    await message.reply(f'Okay, so what will be the new definition for "{to_edit}"?')


@router.message(EditState.new_defition)
async def new_def_handler(message: types.Message, state: FSMContext):
    new_definition = message.text

    state_data = await state.get_data()
    word = state_data['word']

    if new_definition is None:
        await message.reply(
            f'Please, provide me with a new defintiion for "{word}"'
        )

        return

    all_words[word] = new_definition

    await state.clear()
    await message.reply(
        f'The word\'s definition was updated to "{new_definition}"'
    )
