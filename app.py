import os
import time
import yt_dlp
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python app.py <YouTube link> [output_path]")
    sys.exit(1)

yt_url = f"{sys.argv[1]}"
download_path = "./mp3_files"
os.makedirs(download_path, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(yt_url, download=True)
    title = info.get('title', 'video')

    print(f"The quality is: {ydl_opts['format']}")
    print(f"Successfully downloaded and converted: {title}")