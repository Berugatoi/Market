from PIL import Image
import os


def resize_image(image_src):
    im = Image.open(image_src)
    size = (int(os.getenv('IMAGE_WIDTH')), int(os.getenv('IMAGE_HEIGHT')))
    im = im.resize(size)
    im.save(image_src)