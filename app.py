from flask import send_file
from flask import request
from flask import Flask, Response, redirect
import base64
import io
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)


def byteio_to_image(data):
    img = Image.open(BytesIO(base64.b64decode(data)))
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer


@app.route('/')
def index():
    return 'All OK, 200'


# @app.before_request
# def middleware():
#     if request.path.split('/')[1] == 'kvlite':
#         drive = request.full_path.split('/')[2].split(':')[0]
#         file = request.full_path.split(':')[-1][:-1]
#         return redirect(f"/process/{drive}/{file.replace('/', '_')}")


@app.route('/img/<hash>', methods=['GET'])
def get_image(hash):
    base_path = '/home/fs_files/'
    drive, filename = hash.split(':')
    return Response(f'Drive: {drive} File: {filename} File Path: {os.path.join(base_path, drive, filename)}')
    # return Response(, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()
