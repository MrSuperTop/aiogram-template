from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from package.db import all_words

router = Router()

class RemoveState(StatesGroup):
    word = State()


@router.message(Command(commands=['remove']))
async def remove_request_handler(message: types.Message, state: FSMContext):
    await state.set_state(RemoveState.word)
    await message.reply('What is the word you would like to remove?')

@router.message(RemoveState.word)
async def remove_handler(message: types.Message, state: FSMContext):
    to_remove = message.text
    if to_remove is None:
        await message.reply(
            'Please provide a word to remove from the dictionary, see the /list to choose which word to remove'
        )

        await state.clear()
        return

    if to_remove not in all_words:
        await message.reply(
            'Unfortunately, the word you are trying to remove is not present in the dictionary, see the /list'
        )

        await state.clear()
        return

    await state.clear()

    deleted_definition = all_words[to_remove]
    del all_words[to_remove]

    await message.reply(
        f'Successfully removed word "{to_remove}"\nThe defintion was: "{deleted_definition}"'
    )
