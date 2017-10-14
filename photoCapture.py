import os
from flask import Flask, request, Response, jsonify
from PIL import Image
from random import shuffle
import json
#import nexmo
import os
import tweepy
import sys
import time
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
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
    # Consumer keys and access tokens, used for OAuth
    consumer_key = 'iqnii4MjvqSXawfcIo3U5lxsK'
    consumer_secret = 'OrsfgJbBmUrv6FUGY2nCoxsoYTqtPNPmvJ69upNCgsPBAXTACI'
    access_token = '919035545581424640-g7RfSCFb707QbhztMY2Sa94ajrEBzKW'
    access_token_secret = 'TYywGFwLBpGQ8Xl0kwgceNLQRfMsPbOgeVz9EWBwoak1k'

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    # Creates the user object. The me() method returns the user whose authentication keys were used.
    user = api.me()

    print('Hola EU! MLH Photo booth had arrived!')

    # Sample method, used to update a status
    # api.update_status('Hello Form RBI Lab!')

    # load image
    imagePath = "out.png"
    status = "Hi MLH!"

    # Send the tweet.
    api.update_with_media(imagePath, status)

    #delete photos
    os.system("rm 2.jpg")
    os.system("rm 3.jpg")
    os.system("rm 4.jpg")
    os.system("rm out.jpg")
    return True 
if __name__ == "__main__":
    app.run(debug=True)
