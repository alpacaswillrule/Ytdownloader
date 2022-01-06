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
#Starting download, as a mp4

print("Downloading...")
ys.download()

filename = ys.title
slash = '\\'
mp4_name = os.getcwd() + slash + filename + '.mp4'
mp3_name = os.getcwd() + slash + filename + '.mp3'
#converst the mp4 to an mp3 and downloads that.
videoclip = VideoFileClip(mp4_name)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_name)

audioclip.close()
videoclip.close()

print("Download completed")




