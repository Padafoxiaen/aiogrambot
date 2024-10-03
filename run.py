# run.py

import asyncio

# Module without stubs, but it isn't necessary in this project
import betterlogging as logging  # type: ignore

from bot import bot, dp, router
from bot.middlewares import middlewares_list
from service.exception_messages import locale_not_exist
from service.utils import setup_locales, setup_middlewares


async def main(
        locales: list[str] | None,
        init_locales: bool = False
) -> None:

    # Setup logging
    logging.basic_colorized_config(level=logging.INFO)

    # Check if developer wants to just update locales
    if init_locales:
        if locales:
            setup_locales(locales)
            return
        else:
            raise ValueError(locale_not_exist)

    # Other bot settings
    await bot.delete_webhook(drop_pending_updates=True)
    setup_middlewares(middlewares_list, dp)
    dp.include_router(router)

    # Define all handlers
    from bot import handlers  # type: ignore

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main(init_locales=False, locales=['en', 'uk', 'de', 'jp']))
