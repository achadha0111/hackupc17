import os
from flask import Flask, request, Response, jsonify
from PIL import Image
from random import shuffle
import json
#import nexmo
import os
import sys
import time
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def triggerPhotoCapture():
    ''' Insert your photo capture logic here '''

    os.system("gphoto2 --capture-image-and-download" )
    os.system("mv capt0000.jpg 2.jpg")
    time.sleep(5)

    os.system("gphoto2 --capture-image-and-download")
    os.system("mv capt0000.jpg 3.jpg")
    time.sleep(5)

    os.system("gphoto2 --capture-image-and-download")
    os.system("mv capt0000.jpg 4.jpg")
    time.sleep(5)
    #collage making
    images = []
    for line in open("instructions.txt"):
        name = line.split()
        images.append(name[0])
    w, h = Image.open(images[1]).size
    out = Image.new("RGB", (2 * w + 30, 2 * h + 30), "white")

    shuffle(images)
    out.paste(Image.open(images[0]), (10, 10))
    out.paste(Image.open(images[1]), (w + 20, 10))
    out.paste(Image.open(images[2]), (10, h + 20))
    out.paste(Image.open(images[3]), (w + 20, h + 20))
    out.save("out.png")
    ''' Once photos have been captured, call Esraa's function to post to Twitter '''
    return Response(), 200

def postToTwiiter():
    ''' Fill in this function with logic to post to twitter '''
    return True 
if __name__ == "__main__":
    app.run(debug=True)
