# Aiogram Bot

**Aiogram Bot** - a bot that made with **aiogram** library

## 🛠Links

[Aiogram documentary](https://docs.aiogram.dev/en/latest/quick_start.html)
[Asyncio documentary](https://docs.python.org/3/library/asyncio.html)

## 📂Some examples of code
```
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
```
## 💾Example in Telegram
![yo](https://github.com/manixonex/basicaiogrambot/blob/main/aiogram/images/exampletelegram.png)

*[See full code](https://github.com/manixonex/basicaiogrambot/blob/main/aiogram/bot.py)*
