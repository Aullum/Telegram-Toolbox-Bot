from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def charset_keyboard(data: dict) -> InlineKeyboardMarkup:
    charsets = data.get("charsets", {})
    builder = InlineKeyboardBuilder()

    for key, label in [
        ("letters", "Letters (a-z)"),
        ("uppercase", "Uppercase (A-Z)"),
        ("digits", "Digits (0-9)"),
        ("symbols", "Symbols (!@#)"),
    ]:
        state = "✅" if charsets.get(key) else "❌"
        builder.button(text=f"{state} {label}", callback_data=f"toggle:{key}")

    builder.button(text="🔐 Generate Password", callback_data="confirm")
    builder.adjust(1)
    return builder.as_markup()
