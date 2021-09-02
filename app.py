from flask import Flask

# from datetime import date
#from datetime import time
from datetime import datetime, timedelta

app = Flask(__name__)

today = datetime.now()
print("Startup at", today)
sleeptime = today + timedelta(minutes=10)
print("I will sleep till", sleeptime)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/health")
def health():
#    delta = datetime.now() - sleeptime
#    if (delta.days >= 0): 
        return "Ready"
#    else:
#        return "Not Ready", 418