from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.states import FakeProfileState
from bot.keyboards.fake_profile_keyboard import gender_keyboard, locale_keyboard
from bot.services.fake_profile_generator_service import generate_fake_profile
from bot.decorators.finalize_handler import finalize_handler

router = Router()


@router.callback_query(F.data == "tool:fake")
async def start_fake(cb: CallbackQuery, state: FSMContext):
    assert cb.message is not None
    await cb.message.edit_text("🧑 Choose gender:", reply_markup=gender_keyboard())
    await state.set_state(FakeProfileState.choosing_gender)


@router.callback_query(FakeProfileState.choosing_gender, F.data.startswith("gender:"))
async def choose_gender(cb: CallbackQuery, state: FSMContext):
    gender = cb.data.split(":")[1]  # male / female / random
    await state.update_data(gender=gender)
    await state.set_state(FakeProfileState.choosing_locale)
    await cb.message.edit_text("🌍 Choose locale:", reply_markup=locale_keyboard())


@router.callback_query(FakeProfileState.choosing_locale, F.data.startswith("locale:"))
@finalize_handler()
async def choose_locale(cb: CallbackQuery, state: FSMContext):
    locale = cb.data.split(":")[1]  # en_US / ru_RU / etc.
    data = await state.get_data()
    profile = generate_fake_profile(gender=data["gender"], locale=locale)
    await cb.message.edit_text(
        f"🧑 <b>Fake Profile:</b>\n\n{profile}", parse_mode="HTML"
    )
    await state.clear()
