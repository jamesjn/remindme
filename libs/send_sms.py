from twilio.rest import TwilioRestClient
import pymongo
import time
conn = pymongo.Connection('', 27017)

db = conn.remindme
db.authenticate('','')

to_send_list = list(db.reminders.find({'time' : { "$lt": time.time() }}))
db.reminders.remove({'time' : { "$lt": time.time() }})

account = ''
token   = ''

client = TwilioRestClient(account, token)

for to_send_item in to_send_list :
  message = client.sms.messages.create(to="+"+to_send_item['number'], from_="", body=to_send_item['message'])
