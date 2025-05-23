import os
import time
import yt_dlp
import subprocess
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Set up the root window
root = tk.Tk()
root.geometry("900x650")
root.title("YouTube to MP3 Downloader")
root.configure(bg="#f5f5f5")  # Light gray background

# Custom colors
PRIMARY_COLOR = "#4285F4"  # Google blue
SECONDARY_COLOR = "#fbbc05"  # Google yellow
BG_COLOR = "#f5f5f5"
TEXT_COLOR = "#333333"

# Add a header with icon (using emoji as placeholder)
header_frame = tk.Frame(root, bg=BG_COLOR)
header_frame.pack(fill="x", pady=(20, 10))

title_label = tk.Label(
    header_frame, 
    text="YouTube to MP3 Downloader", 
    font=('Helvetica', 24, 'bold'),
    fg=PRIMARY_COLOR,
    bg=BG_COLOR
)
title_label.pack()

subtitle_label = tk.Label(
    header_frame,
    text="Download high-quality audio from YouTube videos",
    font=('Helvetica', 12),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
subtitle_label.pack(pady=(0, 20))

# Create main content frame
content_frame = tk.Frame(root, bg=BG_COLOR)
content_frame.pack(fill="both", expand=True, padx=40, pady=20)

# URL input section
url_frame = tk.Frame(content_frame, bg=BG_COLOR)
url_frame.pack(fill="x", pady=10)

url_label = tk.Label(
    url_frame, 
    text="Enter YouTube URL:", 
    font=('Helvetica', 14),
    anchor="w",
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
url_label.pack(fill="x", pady=(0, 5))

yt_url = tk.StringVar(root)
url_entry = tk.Entry(
    url_frame, 
    textvariable=yt_url,
    font=('Helvetica', 14),
    bd=1,
    relief=tk.SOLID,
    highlightthickness=1,
    highlightcolor=PRIMARY_COLOR
)
url_entry.pack(fill="x", ipady=8)


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
    'ffmpeg_location': './ffmpeg.exe',
}

# Quality selection frame
quality_frame = tk.Frame(content_frame, bg=BG_COLOR)
quality_frame.pack(fill="x", pady=10)

quality_label = tk.Label(
    quality_frame,
    text="Audio Quality:",
    font=('Helvetica', 14),
    anchor="w",
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
quality_label.pack(side=tk.LEFT, padx=(0, 10))

quality_var = tk.StringVar(value="320")
quality_options = ["128", "192", "256", "320"]

# Create a styled combobox
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", 
                fieldbackground=BG_COLOR,
                background=BG_COLOR,
                foreground=TEXT_COLOR,
                arrowcolor=PRIMARY_COLOR)

quality_dropdown = ttk.Combobox(
    quality_frame,
    textvariable=quality_var,
    values=quality_options,
    width=5,
    state="readonly",
    font=('Helvetica', 12),
    style="TCombobox"
)
quality_dropdown.pack(side=tk.LEFT)

quality_label2 = tk.Label(
    quality_frame,
    text="kbps",
    font=('Helvetica', 14),
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
quality_label2.pack(side=tk.LEFT, padx=(5, 0))

# Function to update quality when selection changes
def on_quality_change(*args):
    ydl_opts['postprocessors'][0]['preferredquality'] = quality_var.get()
    
quality_var.trace("w", on_quality_change)


def open_popup():
    popup = tk.Toplevel()
    popup.title("Download Complete")
    popup.configure(bg=BG_COLOR)
    popup.geometry("400x200")
    
    # Make popup appear in center of main window
    popup.transient(root)
    popup.grab_set()
    
    # Success icon (checkmark using Unicode)
    success_icon = tk.Label(
        popup, 
        text="✓", 
        font=('Helvetica', 48),
        fg="#4CAF50",  # Green color
        bg=BG_COLOR
    )
    success_icon.pack(pady=(20, 10))

    # Success message
    success_msg = tk.Label(
        popup, 
        text="Download successfully completed!",
        font=('Helvetica', 14, 'bold'),
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    success_msg.pack(pady=10)

    # Close button with styling
    close_button = tk.Button(
        popup,
        text="Close",
        font=('Helvetica', 12),
        bg=PRIMARY_COLOR,
        fg="white",
        activebackground=SECONDARY_COLOR,
        activeforeground="white",
        relief=tk.FLAT,
        padx=20,
        command=popup.destroy
    )
    close_button.pack(pady=10)
    
    # Center the popup on the main window
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    popup.geometry(f"+{x}+{y}")

def download():
    # Create a container for progress indicators
    progress_frame = tk.Frame(content_frame, bg=BG_COLOR)
    progress_frame.pack(pady=20)
      # Configure progress bar style - use the existing style object
    style.configure("TProgressbar", 
                   background=PRIMARY_COLOR,
                   troughcolor=BG_COLOR,
                   thickness=10)
    
    # Progress bar with styling
    progress = ttk.Progressbar(
        progress_frame,
        orient="horizontal",
        length=500,
        mode="indeterminate"
    )
    progress.pack(pady=10)
    
    # Start animation
    progress.start(15)  # Smoother animation

    # Status message
    status_label = tk.Label(
        progress_frame,
        text="Downloading... Please wait",
        font=('Helvetica', 14),
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    status_label.pack(pady=10)
    
    # Disable download button while processing
    button.config(state=tk.DISABLED)
    
    # Update UI
    root.update()

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(yt_url.get(), download=True)
            title = info.get('title', 'video')

            print(f"The quality is: {ydl_opts['format']}")
            print(f"Successfully downloaded and converted: {title}")

            # Clean up UI
            progress.stop()
            progress_frame.destroy()
            
            # Re-enable download button
            button.config(state=tk.NORMAL)
            
            # Clear the URL field after successful download
            yt_url.set("")
            
            # Show success popup
            open_popup()

    except Exception as e:
        # Show error with better UI
        progress.stop()
        progress_frame.destroy()
        
        # Re-enable download button
        button.config(state=tk.NORMAL)
        
        # Error message with better styling
        error_frame = tk.Frame(content_frame, bg="#FFF4F4")  # Light red background
        error_frame.pack(pady=20, fill="x")
        
        error_icon = tk.Label(
            error_frame,
            text="⚠️",
            font=('Helvetica', 16),
            bg="#FFF4F4",
            fg="#D32F2F"  # Dark red text
        )
        error_icon.pack(side=tk.LEFT, padx=10, pady=10)
        
        error_message = tk.Label(
            error_frame,
            text="Error: Invalid YouTube URL or network issue",
            font=('Helvetica', 12),
            bg="#FFF4F4",
            fg="#D32F2F"
        )
        error_message.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Add a dismiss button
        def dismiss_error():
            error_frame.destroy()
            
        dismiss_btn = tk.Button(
            error_frame,
            text="✕",
            font=('Helvetica', 10),
            bg="#FFF4F4",
            fg="#D32F2F",
            relief=tk.FLAT,
            command=dismiss_error
        )
        dismiss_btn.pack(side=tk.RIGHT, padx=10)


# Download button
button_frame = tk.Frame(content_frame, bg=BG_COLOR)
button_frame.pack(pady=30)

button = tk.Button(
    button_frame,
    text="Download MP3",
    font=('Helvetica', 14, 'bold'),
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=SECONDARY_COLOR,
    activeforeground="white",
    relief=tk.FLAT,
    padx=30,
    pady=10,
    command=download
)
button.pack()

# Footer with instructions
footer_frame = tk.Frame(root, bg=BG_COLOR)
footer_frame.pack(fill="x", side=tk.BOTTOM, pady=15)

footer_text = tk.Label(
    footer_frame,
    text="MP3 files will be saved in the 'mp3_files' folder",
    font=('Helvetica', 10),
    fg="#666666",
    bg=BG_COLOR
)
footer_text.pack()

root.mainloop()