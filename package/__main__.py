import asyncio
import logging

from aiogram import Dispatcher

from package.bot import bot
from package.handlers import router

# TODO: i18n and responses that are defined in a json file
# TODO: DB support with tortoiseORM
# TODO: util function to automatically import all the needed routers in the package.handlers

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    current_loop = asyncio.new_event_loop()
    current_loop.run_until_complete(main())
    
