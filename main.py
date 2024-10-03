import asyncio

# Module without stubs, but it isn't necessary in this project
import betterlogging as logging  # type: ignore

from bot import bot, dp, router


async def main() -> None:
    logging.basic_colorized_config(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)

    # Define all handlers
    from bot import handlers  # type: ignore

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
