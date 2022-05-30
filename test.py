from pytube import YouTube
from flask import Flask, render_template


yt = YouTube("https://www.youtube.com/watch?v=cpB2ZMzXrss")
datas = yt.streams.get_by_itag(139)
print(datas.download())



