import os
from dotenv import load_dotenv
from fastapi import FastAPI
import telebot
from telebot import types

load_dotenv()  # Add this line to load environment variables from the .env file

from config.settings import TELEGRAM_API_TOKEN, OPENAI_API_KEY
from app.chatgpt import generate_response


bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("FastAPI server started")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    user_query = message.text

    response = generate_response(user_query)
    bot.send_message(chat_id, response)

@app.post("/webhook/{token}")
async def webhook_handler(token: str):
    if token != TELEGRAM_API_TOKEN:
        return "Invalid token"

    update = telebot.types.Update.de_json(await app.state.reader.read())
    bot.process_new_updates([update])
    return "OK"
