from pytube import YouTube
from flask import Flask, render_template


yt = YouTube("https://www.youtube.com/watch?v=KLesRVVR_0g")
datas = yt.streams
count = 0
for i in datas:
    if(i.mime_type == "audio/mp4" and i.itag==139):
        print(i)


