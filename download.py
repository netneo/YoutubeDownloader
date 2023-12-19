#!/usr/bin/env python3
from pytube import YouTube
from sys import argv

link = argv[1]
#test_link = "https://www.youtube.com/watch?v=vEQ8CXFWLZU"
video = YouTube(link)
download = video.streams.get_highest_resolution()
video_title = video.title
video_author = video.author
save_folder = "/home/darren/Videos/DownloadedYoutube/"
save_filename = video_title.replace(" ","-")+"----"+video_author.replace(" ", "-")

print(f"Title: {video_title}")
print(f"Author: {video.author}")
print(f"Saving as {save_filename}")
print(f"Saving in {save_folder}")

download.download(save_folder, filename=save_filename)
