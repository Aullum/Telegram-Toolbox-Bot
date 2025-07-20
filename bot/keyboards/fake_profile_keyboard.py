from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def gender_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="♂️ Male", callback_data="gender:male")
    builder.button(text="♀️ Female", callback_data="gender:female")
    builder.button(text="🎲 Random", callback_data="gender:random")
    builder.adjust(2)
    return builder.as_markup()

def locale_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for locale in ["en_US", "ru_RU", "de_DE", "fr_FR", "ja_JP"]:
        builder.button(text=locale, callback_data=f"locale:{locale}")
    builder.adjust(3)
    return builder.as_markup()
