import os
import sys
import yt_dlp
from tqdm import tqdm

def download_videos(links_file):
    if not os.path.exists(links_file):
        print("Error: The links file '{}' does not exist.".format(links_file))
        return
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(autonumber)s - %(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

    with open(links_file, 'r') as f:
        video_links = f.read().splitlines()

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in video_links:
            try:
                info_dict = ydl.extract_info(link, download=True)
                print("\n{}: Download completed!".format(info_dict['title']))
            except Exception as e:
                print("\nError downloading video: {}".format(e))
                continue

if __name__ == "__main__":
    links_file = "links.txt"
    download_videos(links_file)

