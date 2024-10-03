from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from environs import Env

# Creating an own basic environment variable
basic_env = Env()
basic_env.read_env('.env')

# Creating a bot instance
bot_token = basic_env.str('BOT_TOKEN')
if bot_token:
    bot = Bot(
        token=bot_token,
        default=DefaultBotProperties(parse_mode='HTML')
    )
else:
    msg = 'Did you set bot_token in your environments variable?'
    raise ValueError(msg)

# Creating other important instances
dp = Dispatcher()
router = Router()
