from PIL import Image, ImageDraw


def draw(*arguments):
    img = arguments[0]
    color = arguments[1][0]
    width = arguments[1][1]
    points = arguments[1][2]
    dr = ImageDraw.Draw(img)
    dr.line((100, 200, 150, 600), fill=128)
    return img


def crop(*arguments):
    img = arguments[0]
    points = arguments[1][0]
    return img


def resize_abs(*arguments):
    img = arguments[0]
    width, height = arguments[1][0]
    return img


def resize_scale(*arguments):
    img = arguments[0]
    scale = arguments[1][0]
    return img


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
