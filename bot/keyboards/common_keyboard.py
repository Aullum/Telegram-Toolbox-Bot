from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="🛡 Password Generator", callback_data="tool:password"),
        InlineKeyboardButton(text="📂 JSON to CSV", callback_data="tool:json2csv"),
    )
    builder.row(
        InlineKeyboardButton(text="🔤 Base64 Tools", callback_data="tool:base64"),
        InlineKeyboardButton(text="📄 Lorem Ipsum", callback_data="tool:lorem"),
    )
    builder.row(
        InlineKeyboardButton(text="🧑 Fake Profile", callback_data="tool:fake"),
    )

    return builder.as_markup()
