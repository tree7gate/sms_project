from twilio.rest import Client
import os

class Send:
    def __init__(self, acc, token, num):
        self.acc = acc
        self.token = token
        self.num = num
        self.client = Client(self.acc, self.token)


    def send_message(self, city, current, high, low, condition):
        return self.client.messages \
                        .create(
                             body="Welcome to the CT Instant Weather Service! {}'s Current Temperature is: {}F, High: {}F, Low: {}F, Weather Condition: {}".format(city.title(), str(current)+u'\N{DEGREE SIGN}', str(high)+u'\N{DEGREE SIGN}', str(low)+u'\N{DEGREE SIGN}', condition.title()),
                             from_='+17815589918',
                             to=self.num
                         )
