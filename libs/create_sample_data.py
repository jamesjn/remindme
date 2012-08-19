import pymongo
import time
conn = pymongo.Connection('', 27017)

db = conn.remindme
db.authenticate('','')

secs_until_sending_text = range(0, 300, 60)
for secs in secs_until_sending_text:
  db.reminders.insert({'user_id': 1, 'time': time.time() + secs, 'message': 'Sample Message for me in' + str(secs)+ ' secs', 'email': '', 'number': ''})
