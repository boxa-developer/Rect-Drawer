from flask import (
    Flask, Response,
    make_response,
    send_file
)
from PIL import Image
import utils
import json
import os

app = Flask(__name__)


@app.route('/img/<hash_url>/<actions>', methods=['GET'])
def get_image(hash_url, actions):
    base_path = '/home/fs_files/'
    drive, filename = hash_url.split(':')
    file_path = os.path.join(base_path, drive, filename)
    try:
        pill_img = Image.open(file_path)
        acts = ''
        for text in actions.split(':'):
            if text != '':
                acts += text+'-'
                pill_img = utils.action_producer(
                    img=pill_img,
                    action=json.loads(utils.decode_action(text))[0],
                    args=json.loads(utils.decode_action(text))[1:]
                )
        img = utils.pil2buffer(pill_img)
        resp = make_response(send_file(img,
                                       attachment_filename=str(filename + '.jpg'),
                                       mimetype='image/jpeg'))
        resp.headers['Content-Disposition'] = f'inline;filename="{filename}.jpg"'
        resp.headers['action_type'] = acts
        return resp
    except Exception as e:
        return Response(f'<h3 style="color:#ba3939;background:#ffe0e0; '
                        f'border:1px solid  #a33a3a;padding:2px'
                        f'">Error: [ {e} ]</h3>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
