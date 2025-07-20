from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.states import LoremState
from bot.keyboards.lorem_keyboard import lorem_count_keyboard
from bot.services.lorem_generator_service import generate_lorem
from bot.decorators.finalize_handler import finalize_handler

router = Router()

@router.callback_query(F.data == "tool:lorem")
async def lorem_entry(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text("📄 Choose how many paragraphs to generate:", reply_markup=lorem_count_keyboard())
    await state.set_state(LoremState.select_count)

@router.callback_query(LoremState.select_count, F.data.startswith("lorem:"))
@finalize_handler()
async def generate_lorem_handler(cb: CallbackQuery, state: FSMContext):
    count = int(cb.data.split(":")[1])
    text = generate_lorem(count)
    await cb.message.edit_text(f"📝 <b>Lorem Ipsum ({count} paragraphs):</b>\n\n{text}", parse_mode="HTML")
    await state.clear()
