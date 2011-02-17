import unittest
import random
import datetime
from time import sleep
import os

from tweepy import *

"""Configurations"""
# Vous devez fournir les informations d'identification de votre application twitter

consumer_key = CONSUMERKEY
consumer_secret = CONSUMERSECRET

auth = OAuthHandler(consumer_key, consumer_secret)
  
# test pour avoir accès au token
auth_url = auth.get_authorization_url()
print 'S\'il vous plaît autoriser: ' + auth_url
verifier = raw_input('Entrer le code PIN: ').strip()

access_token = auth.get_access_token(verifier)

# construction de l'objet api en utilisant oauth
api = API(auth)


for tweet in range(1,100): # Boucle 100 fois 
    now = datetime.datetime.now()
    dateformat = str(now.strftime('%H:%M:%S le %d-%m-%Y'))
    s = api.update_status('Il est %s  et je suis debout #dakarlug #kebetu #dakar #senegal' %dateformat) #statut
    print tweet
    sleep(300)  # attendre 300 s
