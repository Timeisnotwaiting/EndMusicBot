from pyrogram import Client
from config import *
from pytgcalls import PyTgCalls

alpha = Client(":BOT:", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

yashu = Client(":ASST:", api_id=API_ID, api_hash=API_HASH, string_session=STRING_SESSION)

asst = PyTgCalls(yashu)



