from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

URLs = [
""
]
count = 1
for url in URLs:
    yt = YouTube(url, on_progress_callback=on_progress)
    print("Title:", yt.title)

    # 🎯 Step 1: Get 1080p VIDEO (no audio)
    video_stream = yt.streams.filter(res="1080p", file_extension="mp4").first()

    if not video_stream:
        print("1080p not available for this video")
        exit()

    # 🎯 Step 2: Get AUDIO
    audio_stream = yt.streams.filter(only_audio=True).first()

    # 🎯 Step 3: Download both
    video_file = video_stream.download(filename="video" + str(count) + ".mp4")
    audio_file = audio_stream.download(filename="audio" + str(count) + ".mp4")
    count = count + 1
    print("Downloaded video + audio")
