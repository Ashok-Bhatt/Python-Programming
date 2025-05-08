
from PIL import Image

path = "./american nightmare.jpg"
pathOut = "C:\Users\Ashok Bhatt\Desktop\Web Development Work\Chrome Extensions\Hello World Extension\icons"

image = Image.open(path)
image1 = image.resize((128,128))
image2 = image.resize((48,48))
image3 = image.resize((16,16))

image1.save(pathOut+"\logo1.jpg")
image2.save(pathOut+"\logo2.jpg")
image3.save(pathOut+"\logo3.jpg")