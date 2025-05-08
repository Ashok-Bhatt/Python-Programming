from pytube import Playlist, YouTube
import os
import colorama
from colorama import Back
colorama.init(autoreset=True)

def show_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = ((size - bytes_remaining) / size) * 100
    print(f"{Back.GREEN + ' '*int(progress)} {progress:.2f}%", end='\r')

url = input("Enter YouTube playlist URL: ")
yt = Playlist(url)

playlist_name = yt.title
playlist_owner = yt.owner
total_views = yt.views
total_videos = yt.length
total_length = 0
path = rf"C:\Users\Ashok Bhatt\Videos\{playlist_name} by {playlist_owner}"

for video in yt.videos:
    total_length += video.length


print("Playlist Name: ", playlist_name)
print("Playlist Owner: ", playlist_owner)
print(f"Total Views: {total_views:,}")
print("Total Videos: ", total_videos)
print(f"Total Length: {int(total_length/3600)}:{int((total_length/60)%60)}:{total_length%60}")

want_to_download = input("Want to download all the videos from the given URL? ")

if want_to_download.lower() == "yes":

    for index, video in enumerate(yt.video_urls, start=1):
        yt_video = YouTube(video)
        yt_video.streams.filter(res="480p").first().download(path)
        print(f"\nVideo no {index} downloaded.")

    print("All videos downloaded.")