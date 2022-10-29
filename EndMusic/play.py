from Functions.Youtube import download_audio, download_video

async def play(_, m):
    query = m.text.split(None, 1)[1]
    
