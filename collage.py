from PIL import Image
from random import shuffle

images = []
for line in open("instructions.txt"):
    name = line.split()
    images.append(name[0])

w,h = Image.open(images[1]).size
out = Image.new("RGB", (2*w+30,2*h+30), "white")

shuffle(images)
out.paste(Image.open(images[0]), (10,10))
out.paste(Image.open(images[1]), (w+20,10))
out.paste(Image.open(images[2]), (10,h+20))
out.paste(Image.open(images[3]), (w+20,h+20))
out.save("out.png")
