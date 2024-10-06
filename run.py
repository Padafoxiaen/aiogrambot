# run.py

import asyncio

# Module without stubs, but it isn't necessary in this project
import betterlogging as logging  # type: ignore

from bot import bot, dp, router
from bot.middlewares import middlewares_list
from service.utils import setup_locales, setup_middlewares


async def main() -> None:

    # Check if developer wants to just update locales
    setup_locales(switch=False, locales=['en', 'uk', 'de', 'jp'])

    # Other bot settings
    await bot.delete_webhook(drop_pending_updates=True)
    setup_middlewares(middlewares_list, dp)
    dp.include_router(router)

    # Define all handlers
    from bot import handlers  # type: ignore

    await dp.start_polling(bot)

if __name__ == '__main__':
    # Setup logging
    logging.basic_colorized_config(level=logging.INFO)
    asyncio.run(main())
