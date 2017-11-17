# /usr/bin/python3
# Watcher Plugin to send Pushover Notifications
# Trigger: Snatched Release

import sys
import json
import http.client, urllib
from time import strftime

script, title, year, imdbid, resolution, kind, downloader, downloadid, indexer, info_link, conf_json = sys.argv

conf = json.loads(conf_json)

apikey = conf['apikey']
userkey = conf['userkey']

body = 'Watcher Snatched {} - sent to {} on {}.'.format(title, downloader, strftime("%a, %b %d, at %I:%M%p"))

if conf['channel'] != '':
    body['channel_tag'] = conf['channel']

conn = http.client.HTTPSConnection("api.pushover.net:443")

conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": apikey,
    "user": userkey,
    "message": body,
  }), { "Content-type": "application/x-www-form-urlencoded" })

conn.getresponse()

sys.exit(0)
