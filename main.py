import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

from weather import get_weather


load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message) -> None:
    await message.reply('Welcome! Send me a message containing city name to view current weather!')


@dp.message_handler()
async def send_weather(message: types.Message) -> None:
    weather = get_weather(message.text)
    weather_text = f"{weather['weather_description']}\nTemperature - {weather['temperature']}C\nHumidity - {weather['humidity']}%"
    await message.reply(weather_text)


if __name__ == '__main__':
    executor.start_polling(dp)
