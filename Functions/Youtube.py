from pytube import YouTube

def download_video(url):
    x = YouTube(url)
    try:
        y = x.streams.get_highest_resolution()
        z = y.download()
        return z
    except:
        return None

def download_audio(url):
    x = YouTube(url)
    try:
        y = x.streams.get_audio_only()
        z = y.download()
        return z
    except:
        return None
