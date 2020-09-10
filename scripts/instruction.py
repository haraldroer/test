#!/usr/bin/python3.6
import MySQLdb
import requests
import json
import datetime

db = MySQLdb.connect(host="haraldroer.mysql.pythonanywhere-services.com",
                     user="haraldroer",
                     passwd="michelle44",
                     db="haraldroer$default")

cur = db.cursor()
cur.execute("SELECT text FROM instruction_instruction ORDER BY RAND() LIMIT 1")

random_instruction = str(cur.fetchone()[0])
db.close()
url = 'https://hooks.slack.com/services/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'
headers = {'Content-type': 'application/json'}
data = {"text": random_instruction}
if datetime.datetime.today().weekday() in range(0,5):
    response = requests.post(url, headers=headers, data=json.dumps(data))
