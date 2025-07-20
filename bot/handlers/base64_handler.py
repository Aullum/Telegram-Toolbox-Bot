from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile, Document
from aiogram.fsm.context import FSMContext
from bot.states import Base64State
from bot.keyboards.base64_keyboard import base64_menu
from bot.services.base64_utils_service import encode_text, encode_file, decode_text, decode_file
from bot.decorators.finalize_handler import finalize_handler
import tempfile
import os


router = Router()

@router.callback_query(F.data == "tool:base64")
async def base64_entry(cb: CallbackQuery, state: FSMContext):
    await state.set_state(Base64State.menu)
    await cb.message.edit_text("🔤 Choose an action:", reply_markup=base64_menu())

@router.callback_query(Base64State.menu, F.data.startswith("b64:"))
async def base64_mode_select(cb: CallbackQuery, state: FSMContext):
    mode = cb.data.split(":")[1]  # encode_text, encode_file, etc.
    await state.update_data(mode=mode)

    if mode.endswith("text"):
        await cb.message.edit_text("📥 Send the text:")
        await state.set_state(Base64State.text)
    else:
        await cb.message.edit_text("📤 Upload a file:")
        await state.set_state(Base64State.file)

@router.message(Base64State.text, F.text)
async def handle_text(message: Message, state: FSMContext):
    data = await state.get_data()
    mode = data.get("mode")

    try:
        result = encode_text(message.text) if mode == "encode_text" else decode_text(message.text)
        await message.answer(f"✅ Result:\n<code>{result}</code>", parse_mode="HTML")
        await state.clear()
    except Exception as e:
        await message.answer(f"❌ Error: {str(e)}")

@router.message(Base64State.file, F.document)
@finalize_handler()
async def handle_file(message: Message, state: FSMContext):
    data = await state.get_data()
    mode = data.get("mode")

    try:
        file = await message.bot.download(message.document)
        content = file.read()

        if mode == "encode_file":
            result = encode_file(content)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".b64.txt", mode="w", encoding="utf-8") as tmp:
                tmp.write(result)
                tmp_path = tmp.name
            await message.answer_document(FSInputFile(tmp_path, filename="encoded.b64.txt"))

        elif mode == "decode_file":
            decoded = decode_file(content.decode("utf-8"))
            with tempfile.NamedTemporaryFile(delete=False, suffix=".bin") as tmp:
                tmp.write(decoded)
                tmp_path = tmp.name
            await message.answer_document(FSInputFile(tmp_path, filename="decoded.bin"))

        await state.clear()
        os.remove(tmp_path)

    except Exception as e:
        await message.answer(f"❌ Error: {str(e)}")
