from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")

try:
    yt = YouTube("https://www.youtube.com/watch?v=Z5pq2kYOWTQ")
except:
    print('connection error')

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)


