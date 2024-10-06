# service/utils.py

import subprocess

# Module without stubs
import betterlogging as logging  # type: ignore
from aiogram import Dispatcher
from aiogram_i18n.middleware import I18nMiddleware

from service.exception_messages import locale_not_exist


def setup_locales(switch: bool, locales: list[str]) -> None:
    """
    Function, that simulated a request to aiogram_i18n cli 
    to setup all locales

    Args:
        - locales: list[str]: A list with all names from locales folder that was
        created in 'bot/locales' folder
    """

    if switch:
        if locales:
            cmd = [
                'python', '-m', 'aiogram_i18n', 'multiple-extract', '-i',
                './bot/', '-o', './bot/locales/'
            ]

            for locale in locales:
                cmd.extend(['--locales', locale])

            # Print final command
            logging.info(f"Executing: {' '.join(cmd)}")

            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                logging.error(result.stderr)
                logging.error(
                    f"Command failed with error code {result.returncode}"
                )
            else:
                logging.info(result.stdout)
                logging.info("Command executed successfully")
        else:
            raise ValueError(locale_not_exist)


def setup_middlewares(
        middlewares: list[I18nMiddleware],
        dispatcher: Dispatcher
) -> None:
    for middleware in middlewares:
        if isinstance(middleware, I18nMiddleware):
            middleware.setup(dispatcher)
