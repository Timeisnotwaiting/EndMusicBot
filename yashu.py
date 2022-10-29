from keshav import alpha, asst
from pyrogram import filters, idle
from EndMusic.play import play

@alpha.on_message(filters.command(["play", "vplay"]))
async def play_plug(_, m):
    await play(_, m)

alpha.start()
asst.start()
idle()
