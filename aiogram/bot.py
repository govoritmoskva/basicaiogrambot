import logging
import config

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = (config.token)
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
   await message.reply("Hey!\nI'm ManxnsBot!\nCreated by manixonex.")

@dp.message_handler(commands="info")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Yes", "Nope"]
    keyboard.add(*buttons)
    await message.answer("Want to get some author's information?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Yes")
async def without_puree(message: types.Message):
    await message.reply("Use the /testurl command")

@dp.message_handler(lambda message: message.text == "Nope")
async def without_puree(message: types.Message):
    await message.reply("ok")

@dp.message_handler(commands="testurl")
async def cmd_inline_url(message: types.Message):
    btns = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com/manixonex"),
        types.InlineKeyboardButton(text="Discord", url="https://discord.gg/Djf9umffdF")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*btns)
    await message.answer("Some author's information", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
