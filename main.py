from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="1289650786:AAEDXKavNp3Z80Jy1jjcV8NAkNOUgdvY9wA")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    # text = "Hello"
    # sent_massage = await bot.send_message(chat_id=chat_id, text=text)
    # print(sent_massage.to_python())

    # sent_photo = await bot.send_photo(chat_id=chat_id, photo="https://www.rosphoto.com/images/u/articles/1510/7_5.jpg")
    # print(sent_photo.photo[-1].file_unique_id)


executor.start_polling(dp)
