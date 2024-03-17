import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

# Initializing the Telegram bot and its dispatcher
bot = Bot(token="YOUR_TOKEN_HERE")
dp = Dispatcher(bot)

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Handler for the /start command, providing instructions to the users
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Greetings! This bot facilitates temperature conversion from Celsius to Fahrenheit and vice versa. Please input the temperature you wish to convert.")

# Handler for processing text messages and converting temperatures
@dp.message_handler(content_types=types.ContentType.TEXT)
async def convert_temperature(message: types.Message):
    try:
        temperature = float(message.text)
        response = f"The temperature {temperature}°C converts to {celsius_to_fahrenheit(temperature)}°F"
        response += f"\nThe temperature {temperature}°F converts to {fahrenheit_to_celsius(temperature)}°C"
        await message.reply(response)
    except ValueError:
        await message.reply("Please input a numerical value for temperature.")

if __name__ == "__main__":
    # Initiating the bot's polling mechanism
    aiogram.executor.start_polling(dp)
