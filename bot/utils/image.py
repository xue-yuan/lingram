import logging

from PIL import Image

logger = logging.getLogger(__name__)

def has_correct_size(image: str):
    if ((image.size[0] > 512 or image.size[1] > 512) or 
        (image.size[0] != 512 and image.size[1] != 512)):
        return False
    return True

def resize(original_images: list):
    logger.debug('start to resize image.')
    for original_image in original_images:
        image = Image.open(original_image)
        if has_correct_size(image): continue

        index = 0 if image.size[0] > image.size[1] else 1
        new_size = [None, None]
        new_size[index] = 512
        new_size[0 if index == 1 else 1] = int(image.size[0 if index == 1 else 1] * (512 / image.size[index]))
        image = image.resize(tuple(new_size), Image.ANTIALIAS)
        image.save(original_image, 'png')

    logger.debug('resize successfully.')
