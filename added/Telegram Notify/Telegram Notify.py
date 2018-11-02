# /usr/bin/python3
# Watcher Plugin to send Telegram Notifications
# Trigger: Snatched Release

import sys
import json
import http.client, urllib
from time import strftime

script, title, year, imdbid, resolution, conf_json = sys.argv

conf = json.loads(conf_json)

botid = conf['botid']
chatid = conf['chatid']

body = 'Movie {} ({}) added.'.format(title, year)

conn = http.client.HTTPSConnection("api.telegram.org:443")

conn.request("POST", "/bot{}/sendMessage".format(botid),
  urllib.parse.urlencode({
    "chat_id": chatid,
    "text": body,
  }), { "Content-type": "application/x-www-form-urlencoded" })

conn.getresponse()

sys.exit(0)
