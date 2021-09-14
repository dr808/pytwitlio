## PyTwitlio
Docker container sends an SMS copy of Twitter message when said message contains a word or phrase from list.

For example, if you're trying to catch police pursuits in Los Angeles, `trackwords='pursuit'`, with a Los Angeles news station's Twitter ids. (It's what I use it for anyway).

Another example is to be alerted to @spacex (id: `34743251`) rocket launches (I keep missing them): `trackwords='minus, minutes'`


### Why
Because I don't want the Twitter app on my phone.


### Requirements:
- [Twitter dev account](https://developer.twitter.com/en/apply-for-access)
- [Twilio account](https://twilio.com) with 1 SMS capable phone number and some SMS capable phone number to send SMS to.


### Notes:
- Be careful with which words you allow and especially if you want retweets as this can significantly raise the number of tweets and thus raise cost.
- This can only be used with 1 Twitter dev app at a time. You'll have to create a new app for each concurrent instance.


## Required Vars:
Twitter Words to Track

`TRACKWORDS='pursuit, coronavirus, covid, weather'`

Twitter Accounts to Follow

`TWITTERIDS='9648652, 17379685, 16374678, 24928809, 10252962'`

Twilio To/From #s

`TWILIO_TO_NUMBER='+12125551212'`
`TWILIO_FROM_NUMBER='+12135551212'`

Twilio Sid, Token

`TWILIO_ACCOUNT_SID="ACa0b0c0d0f0e010203040506070809010"`
`TWILIO_AUTH_TOKEN="a0b0c0d0f0e010203040506070809010"`

Twitter Keys, Secrets, etc.

`TWITTER_CONSUMER_KEY='aaaaaaaaaaaaaaaaaaaaaaaaaa'`
`TWITTER_CONSUMER_SECRET='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'`
`TWITTER_ACCESS_TOKEN='1234567890-ccccccccccccccccccccccccccccccccccccccc'`
`TWITTER_ACCESS_TOKEN_SECRET='dddddddddddddddddddddddddddddd'`


### Optional
Allow Retweets

`ALLOW_RT=True`


## Use a service to get Twitter Ids
Something like: http://gettwitterid.com/

## Docker
### Example docker build
`docker build -t pytwitlio .`


### Example Docker Command
```
docker run \
  -dit \
  --restart=always \
  --name pytwitlio\
  -e TWILIO_TO_NUMBER='+12125551212' \
  -e TWILIO_FROM_NUMBER='+12135551212' \
  -e TWILIO_ACCOUNT_SID="ACa0b0c0d0f0e010203040506070809010" \
  -e TWILIO_AUTH_TOKEN="a0b0c0d0f0e010203040506070809010" \
  -e TWITTER_CONSUMER_KEY='aaaaaaaaaaaaaaaaaaaaaaaaaa' \
  -e TWITTER_CONSUMER_SECRET='bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb' \
  -e TWITTER_ACCESS_TOKEN='1234567890-ccccccccccccccccccccccccccccccccccccccc' \
  -e TWITTER_ACCESS_TOKEN_SECRET='dddddddddddddddddddddddddddddd' \
  -e TRACKWORDS='pursuit, coronavirus, covid, weather' \
  -e TWITTERIDS='9648652, 17379685, 16374678, 24928809, 10252962' \
  -e ALLOW_RT=False
  pytwitlio
```
