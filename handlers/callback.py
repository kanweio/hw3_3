from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.config import bot, dp



#@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
     markup = InlineKeyboardMarkup()
     button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
     markup.add(button_call_2)
     question = "Какая порода котов лысая?"
     answers = [
         "Сиамская",
         "Сфинкс",
         "Британец",
     ]
     await bot.send_poll(
         chat_id=call.message.chat.id,
         question=question,
         options=answers,
         is_anonymous=False,
         type='quiz',
         correct_option_id=1,
         open_period=10,
         reply_markup=markup
     )
@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):
    question = "Реальны ли мифы о черных котах?"
    answers = [
        "нет",
        "да",
        "возможно",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=10,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")