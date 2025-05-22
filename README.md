# YouTube to MP3 Converter

A simple and efficient command-line tool to download YouTube videos and convert them to high-quality MP3 files.

## Features

- 🎵 Downloads audio from YouTube videos in the highest quality available
- 🔄 Automatically converts to MP3 format (320kbps quality)
- 📂 Organizes downloads in a dedicated folder
- ⚡ Fast and lightweight

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `yt-dlp`
- FFmpeg (must be placed in the same directory as the script)

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

3. Download [FFmpeg](https://ffmpeg.org/download.html) and place the `ffmpeg.exe` file in the same directory as the script.

## Usage

Run the script with a YouTube URL as an argument:

```
python app.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

⚠️ **Important**: On Windows PowerShell, you must use quotes around URLs that contain special characters like `&`.

The MP3 file will be saved to the `mp3_files` directory with the video's title as the filename.

## How It Works

1. The script takes a YouTube URL as a command-line argument
2. It creates a directory to store the downloaded MP3 files (if it doesn't exist)
3. Using yt-dlp, it downloads the best available audio quality
4. FFmpeg then converts the audio to MP3 format with 320kbps quality
5. The resulting MP3 file is saved with the video's title as the filename

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - For the powerful YouTube download functionality
- [FFmpeg](https://ffmpeg.org/) - For audio conversion capabilities

## Disclaimer

This tool is intended for personal use only. Please respect copyright laws and YouTube's Terms of Service. Only download content that you have permission to download.
