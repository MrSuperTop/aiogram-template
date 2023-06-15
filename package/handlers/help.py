from aiogram import Router, types
from aiogram.filters import Command

HELP_MESSAGE = '''
Here is the list of commands.
None of the commands require any arguments, you will be interactively asked for all of the information needed to perform the wanted action.
\t/help - sends this message
\t/add - adds a word to the dictionary
\t/list - lists all the words that are already present in the dictionary
\t/remove - remove words from the dictionary
\t/edit - edit already present entries
'''

router = Router()

@router.message(Command(commands=['help']))
async def help_handler(message: types.Message):
    await message.reply(HELP_MESSAGE)
