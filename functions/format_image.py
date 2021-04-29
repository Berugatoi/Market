from PIL import Image
import os


def resize_image(image_src):
    im = Image.open(image_src)
    size = (200, 200)
    im = im.resize(size)
    im.save(image_src)