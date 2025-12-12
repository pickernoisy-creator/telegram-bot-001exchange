import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Страны
COUNTRIES = [
    "/USA", "/CANADA", "/UK", "/GERMANY", "/FRANCE", "/SPAIN",
    "/ITALY", "/NETHERLANDS", "/BELGIUM", "/AUSTRIA",
    "/SWITZERLAND", "/UAE"
]

# Языки
def language_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="🇬🇧 English", callback_data="lang_en")
    kb.button(text="🇷🇺 Русский", callback_data="lang_ru")
    kb.button(text="🇪🇸 Español", callback_data="lang_es")
    kb.button(text="🇫🇷 Français", callback_data="lang_fr")
    kb.adjust(1)
    return kb.as_markup()


# Старт
@dp.message(F.text == "/start")
async def start(message: types.Message):
    countries_list = "\n".join(COUNTRIES)
    text = (
        "Welcome to the official bot of the exchange service 001Exchange!\n\n"
        "Please select the country in which you want to make the exchange:\n\n"
        f"{countries_list}"
    )
    await message.answer(text)

# Обработка стран
@dp.message(F.text.in_(COUNTRIES))
async def choose_language(message: types.Message):
    await message.answer("Select the language you want to continue in:", reply_markup=language_keyboard())


# Обработка языков
@dp.callback_query(F.data.startswith("lang_"))
async def languages(callback: types.CallbackQuery):
    lang = callback.data.replace("lang_", "")

    messages = {
        "en": (
            "You have selected the English language for service.\n"
            "If you have questions or would like to make an exchange, contact:\n\n"
            "👤 English-speaking manager: @Anastasia_Lee47"
        ),
        "ru": (
            "Вы выбрали русский язык обслуживания.\n"
            "Для обмена или вопросов свяжитесь с менеджером:\n\n"
            "👤 Русскоязычный менеджер: @Anastasia_Lee47"
        ),
        "es": (
            "Has seleccionado el idioma español.\n"
            "Para cualquier consulta o intercambio, contacta a:\n\n"
            "👤 Gerente hispano: @Anastasia_Lee47"
        ),
        "fr": (
            "Vous avez choisi le français.\n"
            "Pour échanges ou questions, contactez:\n\n"
            "👤 Manager francophone: @Anastasia_Lee47"
        ),
    }

    await callback.message.answer(messages[lang])
    await callback.answer()
