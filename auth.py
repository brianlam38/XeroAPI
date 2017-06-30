#!/usr/bin/python

import json
from xero import Xero
from xero.auth import PrivateCredentials

# Grab RSA and Consumer Key
PRIVATE_KEY_PATH = "../../privatekey.pem"
with open('../../consumer_key.txt', 'r') as myfile:
	CONSUMER_KEY = myfile.read().replace('\n', '')

# Authentication
with open(PRIVATE_KEY_PATH) as keyfile:
	rsa_key = keyfile.read()
credentials = PrivateCredentials(CONSUMER_KEY, rsa_key)
xero = Xero(credentials)