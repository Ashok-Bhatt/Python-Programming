
from pytube import YouTube

url = input("Enter youtube URL: ")
yt = YouTube(url)

print("Title: " , yt.title)
print("View: " , yt.views)
print(f"Length: {int(yt.length/3600)}:{int((yt.length%3600)/60)}:{int(yt.length%60)}")
print("Publish Date: " , yt.publish_date)
print("Owner: " , yt.channel_id)

want_to_download = input("Want to download the video from given URL: ")

if want_to_download.lower() == "yes":
    path = input("Enter path of the downloaded file: ")
    yd = yt.streams.filter(res="360p").first().download(path)