from functools import wraps
from aiogram.types import CallbackQuery
from bot.keyboards.common_keyboard import main_menu_keyboard

def finalize_handler():
    def decorator(func):
        @wraps(func)
        async def wrapper(event: CallbackQuery, *args, **kwargs):
            await func(event, *args, **kwargs)

            if event.message:
                await event.message.answer(
                    "🔧 <b>Choose a tool:</b>",
                    reply_markup=main_menu_keyboard(),
                    parse_mode="HTML"
                )
            return

        return wrapper
    return decorator
