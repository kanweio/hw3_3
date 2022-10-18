from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import bot, ADMINS
from keyboards.client_kb import submit_markup, cancel_markup


# FSM - Finite State Machine

class FSMAdmin(StatesGroup):
    name = State()
    id = State()
    age = State()
    direction = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        else:
            await FSMAdmin.name.set()
            await message.answer(
            f"Привет {message.from_user.full_name}, "
            f"Имя ментора: ",
            reply_markup=cancel_markup
        )
    else:
        await message.answer('Напишите в ЛС')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('id ментора: ')


async def load_id(message: types.Message, state: FSMContext):
    try:
        if not 1 < int(message.text) < 10000000:
            await message.answer('Введите ID!')
            return

        async with state.proxy() as data:
            data['id'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Возраст ментора: ')
    except:
        await message.answer('Используйте числа')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if not 16 < int(message.text) < 100:
            await message.answer('Ментор должен быть старше 16!')
        else:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer('Направление ментора?')
    except:
        await message.answer('Пиши числа!')


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
        await FSMAdmin.next()
        await message.answer('Группа: ')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await bot.send_message(message.from_user.id,
                               f"Имя: {data['name']},  ID: {data['id']}, Возраст: {data['age']},"
                               f"Направление: {data['direction']},"
                               f"Группа: {data['group']}\n")
    await FSMAdmin.next()
    await message.answer('Все верно?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "Да":
        await state.finish()
        await message.answer('Регистрация завершена')
    if message.text.lower() == 'Нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('Пока что не знаем что дальше, ждем следующего урока')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено')


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
