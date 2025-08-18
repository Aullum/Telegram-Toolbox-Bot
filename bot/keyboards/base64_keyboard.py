from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def base64_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="📤 Encode Text", callback_data="b64:encode_text")
    builder.button(text="📥 Decode Text", callback_data="b64:decode_text")
    builder.button(text="📁 Encode File", callback_data="b64:encode_file")
    builder.button(text="📂 Decode File", callback_data="b64:decode_file")

    builder.adjust(2)
    return builder.as_markup()
