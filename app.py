from flask import send_file
from flask import request
from flask import Flask, Response, redirect
import base64
import io
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)


def byte_to_buffer(image):
    # img = Image.open(io.BytesIO(image))
    buffer = io.BytesIO(image)
    # img.save(buffer, format="JPEG")
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
    file_path = os.path.join(base_path, drive, hash)
    with open(file_path, 'rb') as image_file:
        img = image_file
    # return Response(f'Drive: {drive} File: {filename} File Path: {os.path.join(base_path, drive, hash)}')
    return send_file(io.BytesIO(img.read()),
                     attachment_filename=hash+'.jpg',
                     mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
