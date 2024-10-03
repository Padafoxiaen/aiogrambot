# bot/handlers/commands.py

from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot import States, router


@router.message(CommandStart())
async def handle_start(msg: Message, state: FSMContext, i18n: I18nContext) -> None:
    await i18n.set_locale('uk')
    await state.set_state(States.start)
    if msg.from_user:
        await msg.answer(i18n.get('greetings', name=f' {msg.from_user.full_name}'))
