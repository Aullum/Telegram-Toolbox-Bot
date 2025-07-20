from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile, Document
from aiogram.fsm.context import FSMContext
from bot.states import JsonToCsvState
from bot.services.file_converter_service import convert_json_to_csv
from bot.decorators.finalize_handler import finalize_handler
import tempfile
import os

router = Router()

@router.callback_query(F.data == "tool:json2csv")
async def json_entry(cb: CallbackQuery, state: FSMContext):
    await cb.message.edit_text("📤 Please upload a JSON file (array of objects):")
    await state.set_state(JsonToCsvState.waiting_for_file)

@router.message(JsonToCsvState.waiting_for_file, F.document)
@finalize_handler()
async def handle_json_file(message: Message, state: FSMContext):
    document: Document = message.document
    if not document.mime_type == "application/json":
        await message.answer("❌ Only .json files are accepted.")
        return

    try:
        file = await message.bot.download(document)
        json_bytes = file.read()
        csv_bytes = convert_json_to_csv(json_bytes)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp.write(csv_bytes)
            tmp_path = tmp.name

        await message.answer_document(FSInputFile(tmp_path, filename="converted.csv"))
        os.remove(tmp_path)
        await state.clear()

    except Exception as e:
        await message.answer(f"❌ Failed to convert file: {str(e)}")
