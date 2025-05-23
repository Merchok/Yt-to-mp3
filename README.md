# YouTube to MP3 Converter

A simple and efficient tool with graphical interface to download YouTube videos and convert them to high-quality MP3 files.

⚠️ **Note: This application is currently designed for Windows only.**

## Features

- 🎵 Downloads audio from YouTube videos in the highest quality available
- 🎚️ Choose audio quality (128, 192, 256, or 320 kbps)
- 🖥️ User-friendly graphical interface
- 🔄 Automatically converts to MP3 format
- 📂 Organizes downloads in a dedicated folder
- ⚡ Fast and lightweight

## Requirements

- Windows operating system
- Python 3.6 or higher
- Required Python packages:
  - `yt-dlp`
  - `tkinter` (usually included with Python on Windows)
- FFmpeg.exe file in the app folder

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/yt-to-mp3.git
   cd yt-to-mp3
   ```

2. Install required Python packages:
   ```
   pip install yt-dlp
   ```

3. Download FFmpeg (if not included):
   - Download FFmpeg from the [official website](https://ffmpeg.org/download.html)
   - For Windows:
     - Download the "Windows builds" from gyan.dev
     - Extract the zip file
     - Copy the `ffmpeg.exe` file from the `bin` folder
     - Paste it in the same directory as `app.py`
   
   Alternatively, you can use this PowerShell command to download it automatically:
   ```powershell
   Invoke-WebRequest -Uri "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip" -OutFile "ffmpeg.zip"
   Expand-Archive -Path "ffmpeg.zip" -DestinationPath "ffmpeg_temp"
   $ffmpegPath = (Get-ChildItem -Path "ffmpeg_temp" -Recurse -Filter "ffmpeg.exe").FullName
   Copy-Item -Path $ffmpegPath -Destination "ffmpeg.exe"
   Remove-Item -Path "ffmpeg_temp" -Recurse
   Remove-Item -Path "ffmpeg.zip"
   ```

## Usage

Run the application:

```
python app.py
```

Then:
1. Enter a YouTube URL in the text field
2. Select your preferred audio quality
3. Click the "Download MP3" button

The MP3 file will be saved to the `mp3_files` directory with the video's title as the filename.

## How It Works

1. The application provides a user-friendly interface for downloading YouTube audio
2. It creates a directory to store the downloaded MP3 files (if it doesn't exist)
3. Using yt-dlp, it downloads the best available audio quality
4. FFmpeg then converts the audio to MP3 format with your selected quality (128-320kbps)
5. The resulting MP3 file is saved with the video's title as the filename

## Security Considerations

- This application uses `yt-dlp` and `FFmpeg`, both established and trusted open-source projects
- The application doesn't collect any personal data or send information to external servers
- Downloaded files are saved only to the local `mp3_files` directory
- The application doesn't require administrative privileges to run
- FFmpeg executable is included in the repository for convenience

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - For the powerful YouTube download functionality
- [FFmpeg](https://ffmpeg.org/) - For audio conversion capabilities

## Disclaimer

This tool is intended for personal use only. Please respect copyright laws and YouTube's Terms of Service. Only download content that you have permission to download.
