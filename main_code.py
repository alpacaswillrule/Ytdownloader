from pytube import YouTube
import sys
import os
from moviepy.editor import *

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")

try:
    yt = YouTube(link)
except:
    print('connection error')

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
video = VideoFileClip(os.path.join("path","to","movie.mp4"))
video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))
print("Download completed")