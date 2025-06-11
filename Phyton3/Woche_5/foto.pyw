from PIL import Image
im = Image.open("SM_2.jpg")
print(im.mode)
im.show

from PIL import Image
im = Image.new(mode="L", size=(200,100), color=190)
print(im.mode)
im.show