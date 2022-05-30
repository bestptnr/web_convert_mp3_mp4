from pytube import YouTube
from flask import Flask, render_template,request,url_for

app = Flask(__name__)
@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("index.html",data="")
    if request.method == "POST":
        dic = dict()
        src = request.form['url']
        new_src = src.split("=")
        url = "https://www.youtube.com/embed/"+new_src[1]
        yt = YouTube(src)
        mp3 = yt.streams.get_by_itag(139)
        mp4 = yt.streams.get_by_itag(22)
        dic = {"url":url,"mp3":mp3.url,"mp4":mp4.url}
        return render_template("index.html",data=dic)

if __name__ == "__main__":
    app.run(debug=True)

