from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from package.db import all_words

router = Router()


class AddForm(StatesGroup):
    word = State()
    definition = State()


@router.message(Command(commands=['add']))
async def add_word_handler(message: types.Message, state: FSMContext):
    await state.set_state(AddForm.word)
    await message.reply(
        'Please, send me the word your would like to add to the dictionary!'
    )


@router.message(Command(commands=['cancel']))
async def cancel_handler(message: types.Message, state: FSMContext):
    if state.get_state() is None:
        return

    await state.clear()
    await message.reply('Cancelled.')


@router.message(AddForm.word)
async def add_name(message: types.Message, state: FSMContext):
    if message.text in all_words:
        await message.reply(
            'This word is already defined in the dictionary, give me another one or /cancel and try /edit to edit the definition'
        )

        return

    await state.update_data(word=message.text)
    await state.set_state(AddForm.definition)

    await message.reply('Nice! What\'s the definition then?')


@router.message(AddForm.definition)
async def add_definition(message: types.Message, state: FSMContext):
    await state.update_data(definition=message.text)
    all_data = await state.get_data()
    await state.clear()

    word, definition = all_data['word'], all_data['definition']

    all_words[word] = definition
    await message.reply(f'Great! Added word: "{word}"\nDefined as "{definition}"')
