import yt_dlp
import os.path

url = input("Enter video url: ")
ydl_opt = {}


with yt_dlp.YoutubeDL(ydl_opt) as ydl:
    ydl.download([url])

print("Video downloaded successfully")