from aiogram import Bot, Dispatcher, executor, types

from package.config import config

bot = Bot(config.telegram_token)
dp = Dispatcher(bot)

all_words = {}


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message) -> None:
    await message.reply('Hi!\nI am a TestBot')


@dp.message_handler(commands=['add'])
async def add_word(message: types.Message):
    args = message.get_args()
    if args is None:
        return

    word, definition = args.split(' ')
    all_words[word] = definition

    await message.reply(f'Added {word} = {definition}')


@dp.message_handler(commands=['list'])
async def send_list(message: types.Message) -> None:
    if len(all_words) == 0:
        await bot.send_message(
            message.chat.id,
            'The list is empty... Add a word using /add'
        )

        return

    lines = []
    for index, (word, definition) in enumerate(all_words.items()):
        lines.append(f'{index + 1}. {word}: {definition}')

    message_text = '\n'.join(lines)
    await bot.send_message(message.chat.id, message_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
