from flask import *
import pymongo
from dateutil.parser import *
from datetime import *
import os
app = Flask(__name__)
if os.environ.has_key('DEVELOPMENT'):
  app.debug = True
  conn = pymongo.Connection()
  db = conn.remindme
else:
  conn = pymongo.Connection('', 27017)
  db = conn.remindme
  db.authenticate('','')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/incoming", methods=['GET', 'POST'])
def incoming():
    print "incoming"
    print request.method
    if request.method == "POST":
        print 'post got,'
        print request.form.items()
        number = request.form.get('to').split("@")[0]
        text = request.form.get('subject').split("at")
        message, time = [x.strip() for x in text]
        time = int(parse(time).strftime('%s'))
        db.reminders.insert({"message":message, "time":time, "number":number})
        print message, time, number
    return "yay"

@app.route("/user/<int:user_id>/reminders")
def show_reminders(user_id):
  reminders = list(db.reminders.find())
  return render_template('show_reminders.html', reminders=reminders)

if __name__ == "__main__":
    app.run()
