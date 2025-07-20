from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

def lorem_count_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for count in [1, 3, 5, 10, 15]:
        builder.button(text=f"{count} paragraphs", callback_data=f"lorem:{count}")
    builder.adjust(2)
    return builder.as_markup()
