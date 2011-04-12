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
    Date=datetime.datetime(2011,03,25,20,30,00,0)
    now = datetime.datetime.now()
    diff = Date-now
    print diff
    #dateformat = str(diff.strftime('%H:%M:%S'))
    s = diff.seconds+3600
    # hours
    hours = s // 3600 
    # remaining seconds
    s = s - (hours * 3600)
    # minutes
    minutes = s // 60
    # remaining seconds
    seconds = s - (minutes * 60)
    # total time
    if hours >0:
        s = api.update_status('%sh:%smn:%ss Avant le [DakarLUG] GeekDinner #dakarlug #linux #dakar #senegal #fb' % (hours, minutes, seconds)) #statut
        sleep(600)  # attendre 600 s
    else:
        if minutes > 0 :
            s = api.update_status('%smn:%ss Avant le [DakarLUG] GeekDinner #dakarlug #linux #dakar #senegal #fb' % (minutes, seconds)) #statut
            sleep(300)  # attendre 300 s
        else:
            if s > 0 :
                s = api.update_status('%ss Avant le [DakarLUG] GeekDinner #dakarlug #linux #dakar #senegal #fb' % (seconds)) #statut
                sleep(30)  # attendre 30 s
            else:
                break
            
    print tweet

