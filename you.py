from pytube import YouTube
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    yt = YouTube("https://www.youtube.com/watch?v=cpB2ZMzXrss")
    datas = yt.streams
    return render_template("index.html",data=datas)

if __name__ == "__main__":
    app.run(debug=True)

