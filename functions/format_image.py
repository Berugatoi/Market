from PIL import Image
import os
from uuid import uuid5, NAMESPACE_OID


def resize_image(image_src):
    try:
        im = Image.open(image_src)
        size = (200, 200)
        im = im.resize(size)
        im.save(image_src)
    except:
        pass