import pafy
import os
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.chat.id,
                           "Hi, you can share the link of the video from where you want to get mp3 file(/get_music)")


@dp.message_handler(commands=['get_music'])
async def get_music(msg: types.Message):
    await bot.send_message(msg.chat.id, "Share the url")


@dp.message_handler(lambda x: "youtube.com" in x.text)
async def downloading(msg: types.Message):
    await bot.send_message(msg.chat.id, "Wait, it takes time...")
    url = msg.text
    audio = None
    try:
        video = pafy.new(url)
        best = video.getbestaudio().download()
        path = '.'
        files = os.listdir(path)
        for filename in files:
            if video.title in filename:
                audio = filename
                break

        await bot.send_audio(msg.chat.id, open(audio, "rb"))
    except Exception :
        await bot.send_message(msg.chat.id, "Currently service cannot provide mp3 file")


executor.start_polling(dp)
