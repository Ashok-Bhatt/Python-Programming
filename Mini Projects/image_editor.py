
from PIL import Image, ImageEnhance, ImageFilter
from PIL.ImageFilter import CONTOUR

path = "./american nightmare.jpg"
pathOut = path

image = Image.open(path)
image.show()    # shows the image in the gallery

edited_image = image.filter(CONTOUR).rotate(-180)
edited_image.show()

enhancer = ImageEnhance.Brightness(edited_image)
enhanced_image = enhancer.enhance(3)
edited_image.show()