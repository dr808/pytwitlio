import twilioclient as twilio
import twitterclient as twitter
import sys

print('python version: ', sys.version)


# Tweepy Stream Listener
class MyStreamListener(twitter.tweepy.StreamListener):
    def on_status(self, status):
        # Prints tweet if one of the trackwords are in it
        if not twitter.allow_rt:
            if not str(status.text).startswith('RT'):
                if any(word in status.text.lower() for word in twitter.trackwords):
                    message = twilio.client.messages.create(
                        body=status.text,
                        from_=twilio.from_number,
                        to=twilio.to_number
                    )
                    # print(message.sid)
                    print(status.text)
        else:
            if any(word in status.text.lower() for word in twitter.trackwords):
                message = twilio.client.messages.create(
                    body=status.text,
                    from_=twilio.from_number,
                    to=twilio.to_number
                )
                # print(message.sid)
                print(status.text)

    def on_error(self, status_code):
        # when status_code=420, returning False disconnects stream
        print('Twitter Error: ', status_code)
        return False


# Init Listener
myStreamListener = MyStreamListener()
myStream = twitter.tweepy.Stream(auth=twitter.api.auth, listener=myStreamListener)


# Print Status
print('Following: ', twitter.twitterids)
print('Trackwords: ', twitter.trackwords)
print('To: ', twilio.to_number, 'From: ', twilio.from_number)
print('Allow RT?: ', twitter.allow_rt)


# Do it
myStream.filter(follow=twitter.twitterids)
