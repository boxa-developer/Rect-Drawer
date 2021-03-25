from flask import send_file
from flask import request
from flask import Flask, Response, redirect
import base64
import io
from PIL import Image, ImageDraw
from io import BytesIO
import os
import json
import operations

app = Flask(__name__)


@app.route('/')
def index():
    return 'All OK, 200'


def decode_action(text):
    base64_string = text
    base64_bytes = base64_string.encode("utf-8")
    text_bytes = base64.b64decode(base64_bytes)
    text_string = text_bytes.decode("utf-8")
    return text_string


def pil2buffer(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG')
    img_io.seek(0)
    return img_io


@app.route('/img/<hash_url>/<actions>', methods=['GET'])
def get_image(hash_url, actions):
    base_path = '/home/fs_files/'
    # drive, filename = hash_url.split(':')
    file_path = os.path.join(base_path, 'd0', hash_url)
    # with open(file_path, 'rb') as image_file:
    #     img = io.BytesIO(image_file.read())
    #     Image.frombuffer()
    pill_img = Image.open(file_path)
    # for text in actions.split(':'):
    #     img = operations.action_producer(
    #         img=img,
    #         action=json.loads(decode_action(text))[0],
    #         args=json.loads(decode_action(text))[1:]
    #     )

    img = pil2buffer(pill_img)

    return send_file(img,
                     attachment_filename=str(hash_url + '.jpg'),
                     mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
