import os
from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        format_choice = request.form.get("format")

        try:
            ydl_opts = {
                'format': 'bestaudio/best' if format_choice == 'audio' else 'best',
                'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
                'noplaylist': True,
                'quiet': True
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            return send_file(filename, as_attachment=True)

        except Exception as e:
            return f"<h2>Error: {str(e)}</h2>"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
