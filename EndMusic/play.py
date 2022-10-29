from Functions.Youtube import download_audio, download_video
from keshav import asst
from pytgcalls.types import AudioPiped, AudioVideoPiped 

async def play(_, m):
    query = m.text.split(None, 1)[1]
    video = True if m.text.split()[0][1] == "v" else False
    try:
        x = download_video(query) if video else download_audio(query)
        await asst.join_group_call(m.chat.id, AudioVideoPiped(x) if video else AudioPiped(x))
    except:
        pass
