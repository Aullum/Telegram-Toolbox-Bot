from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.keyboards.common_keyboard import main_menu_keyboard

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "🔧 <b>Welcome to Telegram Toolbox Bot!</b>\n\nChoose a tool:",
        reply_markup=main_menu_keyboard(),
        parse_mode="HTML"
    )
