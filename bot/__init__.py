from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage
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
    msg = 'Did you set bot token in your environments variable?'
    raise ValueError(msg)

# Creating other important instances
redis_port = basic_env.int('REDIS_PORT')
redis_host = basic_env.str('REDIS_HOSTNAME')

dp = Dispatcher(storage=RedisStorage.from_url(
    f'redis://{redis_host}:{redis_port}/0'
))

router = Router()


# Create class with bot states
class States(StatesGroup):
    start = State()
