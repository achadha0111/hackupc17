import os
from flask import Flask, request, Response, jsonify
import json
import nexmo
import sys
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def triggerPhotoCapture():
    ''' Insert your photo capture logic here '''
	


    ''' Once photos have been captured, call Esraa's function to post to Twitter '''
    return Response(), 200

def postToTwiiter():
    ''' Fill in this function with logic to post to twitter '''
    return True 
if __name__ == "__main__":
    app.run(debug=True)
