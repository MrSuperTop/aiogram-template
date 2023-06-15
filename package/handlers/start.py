from aiogram import Router, types
from aiogram.filters import CommandStart

from package.bot import bot

router = Router()
@router.message(CommandStart())
async def start_handler(message: types.Message):
    me = await bot.me()

    greeting_name = f'@{me.username}' if me.username is not None else me.first_name
    await message.reply(
        f'Hello and welcome! I am {greeting_name}.\nStart your journey with /help'
    )
