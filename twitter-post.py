import tweepy
import os

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
imagePath = "EsraaDandash/Desktop/mlh.jpg"
status = "Hi MLH!"

# Send the tweet.
api.update_with_media(imagePath, status)
