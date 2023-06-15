from aiogram import Router, types
from aiogram.filters import Command

from package.db import all_words

router = Router()

@router.message(Command(commands=['list']))
async def send_list(message: types.Message) -> None:
    if len(all_words) == 0:
        await message.reply('The list is empty... Add a word using /add')

        return

    lines = []
    for index, (word, definition) in enumerate(all_words.items()):
        lines.append(f'{index + 1}. {word}: {definition}')

    message_text = '\n'.join(lines)
    await message.reply(message_text)
