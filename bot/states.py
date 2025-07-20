from aiogram.fsm.state import StatesGroup, State

class PasswordState(StatesGroup):
    length = State()
    options = State()

class JsonToCsvState(StatesGroup):
    waiting_for_file = State()

class Base64State(StatesGroup):
    menu = State()
    text = State()
    file = State()

class LoremState(StatesGroup):
    select_count = State()

class FakeProfileState(StatesGroup):
    choosing_gender = State()
    choosing_locale = State()