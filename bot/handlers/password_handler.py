from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.states import PasswordState
from bot.keyboards.password_keyboard import charset_keyboard
from bot.services.password_generator_service import generate_secure_password
from bot.decorators.finalize_handler import finalize_handler
import html

router = Router()

@router.callback_query(F.data == "tool:password")
async def password_entry(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text("🔢 Enter desired password length (4–100):")
    await state.set_state(PasswordState.length)

@router.message(PasswordState.length, F.text.regexp(r"^\d{1,3}$"))
async def password_set_length(message: Message, state: FSMContext):
    length = int(message.text)
    if not 4 <= length <= 100:
        await message.answer("⚠️ Length must be between 4 and 100.")
        return
    await state.update_data(length=length, charsets={
        "letters": True,
        "uppercase": True,
        "digits": True,
        "symbols": True,
    })
    await state.set_state(PasswordState.options)
    await message.answer("✅ Choose character sets to include:", reply_markup=charset_keyboard(await state.get_data()))

@router.callback_query(PasswordState.options, F.data.startswith("toggle:"))
async def toggle_charset(cb: CallbackQuery, state: FSMContext):
    if not cb.data:
        await cb.answer("❗ Invalid selection", show_alert=True)
        return
    
    key = cb.data.split(":")[1]
    data = await state.get_data()
    data["charsets"][key] = not data["charsets"][key]
    await state.update_data(charsets=data["charsets"])
    await cb.message.edit_reply_markup(reply_markup=charset_keyboard(data))

@router.callback_query(PasswordState.options, F.data == "confirm")
@finalize_handler()
async def generate(cb: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    selected = [k for k, v in data["charsets"].items() if v]
    if not selected:
        await cb.answer("❗ Select at least one character set", show_alert=True)
        return

    password = generate_secure_password(
        length=data["length"],
        charsets=data["charsets"]
    )
    escaped = html.escape(password)
    await cb.message.edit_text(f"🔐 <b>Generated password</b> ({data['length']} chars):\n\n<code>{escaped}</code>", parse_mode="HTML")
    await state.clear()
