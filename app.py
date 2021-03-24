from flask import send_file
from flask import request
from flask import Flask, Response, redirect
import base64
import io
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'All OK, 200'


@app.route('/img/<hash_url>', methods=['GET'])
def get_image(hash_url):
    base_path = '/home/fs_files/'
    drive, filename = hash_url.split(':')
    file_path = os.path.join(base_path, drive, hash_url)
    with open(file_path, 'rb') as image_file:
        img = io.BytesIO(image_file.read())
    return send_file(img,
                     attachment_filename=str(hash_url + '.jpg'),
                     mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
