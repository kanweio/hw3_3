from aiogram import types, Dispatcher
from handlers.config import bot, ADMINS
import random


#@dp.message_handler()
async def echo(message: types.Message):
    dices = ['⚽️', '🏀', '🎯', '🎳', '🎰', '🎲']
    if message.text == 'game':
        if message.chat.type != 'private':
            if not message.from_user.id in ADMINS:
                await message.reply('ты не мой босс!')
            else:
                await  bot.send_dice(message.chat.id, emoji=random.choice(dices))
        else:
            print('Пиши в группу!')
    else:
        if message.text.isnumeric():
            if len(message.text) > 3:
                await message.answer('я не буду это умножать мне лень')
            else:
                await message.answer(int(message.text) ** 2)
        else:
            await bot.send_message(message.chat.id, message.text)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
