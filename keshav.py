from pyrogram import Client, idle
from config import *
from pytgcalls import PyTgCalls

alpha = Client(":BOT:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

yashu = Client(":ASST:", api_id=API_ID, api_hash=API_HASH, string_session=STRING_SESSION)

x = PyTgCalls(yashu)



alpha.start()
x.start()
idle()
