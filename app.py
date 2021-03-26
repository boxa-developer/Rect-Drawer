from flask import send_file
from flask import request
from flask import make_response
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
    drive, filename = hash_url.split(':')
    file_path = os.path.join(base_path, drive, filename)
    try:
        pill_img = Image.open(file_path)
        for text in actions.split(':'):
            if text != '':
                pill_img = operations.action_producer(
                    img=pill_img,
                    action=json.loads(decode_action(text))[0],
                    args=json.loads(decode_action(text))[1:]
                )
        img = pil2buffer(pill_img)
        resp = make_response(send_file(img,
                                       attachment_filename=str(filename + '.jpg'),
                                       mimetype='image/jpeg'))
        resp.headers['Content-Disposition'] = f'inline;filename="{filename}.jpg"'
        return resp
    except Exception as e:
        return Response(f'<h3 style="color: red">Cannot Open Image  with error {e}</h3>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
