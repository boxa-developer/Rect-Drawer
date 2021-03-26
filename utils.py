from PIL import Image, ImageDraw, ImageColor
from io import BytesIO
import base64


def action_producer(**kwargs):
    image = kwargs.get('img')
    args = kwargs.get('args')
    if kwargs.get('action') == 'draw':
        image = draw(image, args)
    elif kwargs.get('action') == 'crop':
        image = crop(image, args)
    elif kwargs.get('action') == 'abs':
        image = resize_abs(image, args)
    elif kwargs.get('action') == 'scale':
        image = resize_scale(image, args)
    return image


def draw(*arguments):
    img = arguments[0]
    color = arguments[1][0]
    width = arguments[1][1]
    points = arguments[1][2]
    points_tuple = []
    for point in points:
        points_tuple += [point[0], point[1]]
    dr = ImageDraw.Draw(img)
    dr.line(tuple(points_tuple),
            fill=ImageColor.getrgb(color),
            width=width)
    return img


def crop(*arguments):
    img = arguments[0]
    points = arguments[1][0]
    points_tuple = []
    for point in points:
        points_tuple += [point[0], point[1]]
    img = img.crop(tuple(points_tuple))
    return img


def resize_abs(*arguments):
    img = arguments[0]
    width, height = arguments[1][0]
    img.resize((width, height), Image.ANTIALIAS)
    return img


def resize_scale(*arguments):
    img = arguments[0]
    scale = arguments[1][0]
    width, height = img.size

    return img


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
