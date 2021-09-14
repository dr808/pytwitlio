from twilio.rest import Client
import os
import sys


# Init Twilio Vars
try:
    # Sets Twilio To #
    to_number = os.environ['TWILIO_TO_NUMBER']
except KeyError:
    sys.exit('Must supply valid Twilio To Numnber. See Readme')

try:
    # Sets Twilio From #
    from_number = os.environ['TWILIO_FROM_NUMBER']
except KeyError:
    sys.exit('Must supply valid Twilio To Numnber. See Readme')

try:
    # Sets Twilio Account Sid & Auth Token
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
except KeyError:
    sys.exit('Failed setting Twilio Auth, Sid, or both')


# Initialize Twilio
try:
    client = Client(account_sid, auth_token)
except KeyError:
    sys.exit('Failed to init Twilio Client')
