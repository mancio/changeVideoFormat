# Video Converter Script

## Overview
This Python script converts all video files in a given folder to **MKV format** using **FFmpeg** with **NVIDIA GPU acceleration (NVENC)**. It maintains high-quality video while copying the original audio stream.

## Features
- Converts videos from **MP4, AVI, MOV, WMV, FLV, M4V** to **MKV**
- Utilizes **NVIDIA GPU (CUDA) hardware acceleration** for faster encoding
- Uses **H.264 (NVENC)** codec for efficient compression
- Preserves **original audio** without re-encoding
- Ensures **fast playback optimization** using `+faststart`

## Requirements
- **Python 3.x**
- **FFmpeg** installed with NVIDIA support (`h264_nvenc` encoder)
- **NVIDIA GPU** with CUDA support

## Installation
1. **Install FFmpeg** (if not already installed):
   - On Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to the system PATH.
   - On Linux (Debian/Ubuntu):
     ```sh
     sudo apt update && sudo apt install ffmpeg
     ```
   - On macOS (using Homebrew):
     ```sh
     brew install ffmpeg
     ```
2. **Ensure NVIDIA GPU drivers are installed**
3. **Install Python dependencies (if required)**:
   ```sh
   pip install subprocess
   ```

## Usage
Run the script from the terminal or command prompt:
```sh
python main.py <folder_path>
```

### Example:
```sh
python main.py "C:\Users\YourName\Videos"
```
This will convert all compatible videos in the specified folder to **MKV format**.

## Customization
- Change the `video_format` variable to a different format (e.g., `.mp4`, `.mov`)
- Modify the FFmpeg settings to adjust compression speed/quality

## Notes
- This script **does not** overwrite original files; it creates new `.mkv` files.
- GPU encoding (`h264_nvenc`) significantly speeds up conversion compared to CPU-based encoding.
- If you experience issues, ensure your **NVIDIA GPU drivers and FFmpeg NVENC support** are correctly installed.
