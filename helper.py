# Optional YouTube audio helper. Run it on the same device as your browser.
# Setup:  pip install flask flask-cors yt-dlp   (ffmpeg must be installed too)
# Run:    python helper.py      -> serves http://localhost:8787
# Only use it for audio you own or have permission to use.
import subprocess, tempfile, glob
from flask import Flask, request, send_file, abort
from flask_cors import CORS
app = Flask(__name__); CORS(app)

@app.route('/audio')
def audio():
    url = request.args.get('url', '')
    if not url.startswith('http'):
        abort(400)
    d = tempfile.mkdtemp()
    subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '--no-playlist',
                    '-o', d + '/a.%(ext)s', url], check=True)
    return send_file(glob.glob(d + '/a.*')[0])

app.run(port=8787)
