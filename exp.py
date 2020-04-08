from PIL import *
img = Image.open("japan.png")
print(img.format, img.size, img.mode)