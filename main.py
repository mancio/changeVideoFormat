import os
import subprocess
import sys

video_format = ".mkv"

def convert_videos_to_mkv(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.avi', '.mov', '.wmv', '.flv', '.m4v')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, os.path.splitext(filename)[0] + video_format)
            subprocess.run([
                'ffmpeg', '-y', '-hwaccel', 'cuda', '-i', input_path,
                '-c:v', 'h264_nvenc', '-preset', 'slow', '-cq', '18',
                '-c:a', 'copy', '-movflags', '+faststart', output_path
            ], stderr=subprocess.DEVNULL)
            print(f"Converted: {filename} to {video_format}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    convert_videos_to_mkv(folder_path)