from aiogram import types, Dispatcher
from handlers.config import bot, ADMINS


async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            await message.answer(f"{message.from_user.first_name} закрепил(а) сообщение "
                                 f"{message.reply_to_message.from_user.full_name}")



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')