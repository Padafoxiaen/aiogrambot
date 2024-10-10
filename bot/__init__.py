from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage

from data import transporter as t

# Creating a bot instance
bot_token = t.bot.BOT_TOKEN
if bot_token:
    bot = Bot(
        token=bot_token,
        default=DefaultBotProperties(parse_mode='HTML')
    )
else:
    msg = 'Did you set a bot token in your environments variable?'
    raise ValueError(msg)

# Creating other important instances
dp = Dispatcher(storage=RedisStorage.from_url(
    f'redis://default:{t.redis.REDIS_PASSWORD}'
    f'@{t.redis.REDIS_IP}:{t.redis.REDIS_PORT}/{t.redis.REDIS_DATABASE}'
))

router = Router()


# Create class with bot states
class States(StatesGroup):
    start = State()
