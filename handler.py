import base64
import io
from PIL import Image
from io import BytesIO


class ProcImage(object):
    def __init__(self):
        pass

    def download_image(self, url):
        pass

    def byteio_to_image(self):
        with open('img_str', 'r') as img_file:
            data = base64.b64encode(img_file.read())

        file_like = io.StringIO(data)

        img = PIL.Image.open(file_like)
        img.show()

    def image_to_byteio(self):
        pass

    def draw(self):
        pass

    def crop(self):
        pass


def byteio_to_image():
    tim = None
    with open('img_str', 'rb') as img_file:
        data = img_file.read()
    img = Image.open(BytesIO(base64.b64decode(data)))
    img.save('image.png', 'PNG')


byteio_to_image()
