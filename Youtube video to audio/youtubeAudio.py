from pytube import YouTube
import os
# url input from user
yt = YouTube (input("Enter the URL of the video you want to download: \n>> "))
# extract only audio
video = yt.streams.filter (only_audio=True). first()


# download the file
out_file = video.download ()
# save the file
base, ext = os.path.splitext (out_file)
new_file = base + '.mp3'
os. rename (out_file, new_file)
# result of success
print (yt.title + " has been successfully downloaded.")






















# import pytube

# url="https://www.youtube.com/watch?v=uYPbbksJxIg&t=5s"
# youtube=pytube.YouTube(url)

# stream=youtube.streams.get_audio_only()

# stream.download()