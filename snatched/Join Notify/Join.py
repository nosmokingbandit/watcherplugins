# /usr/bin/python3
# Watcher Plugin to send Join Notifications
# Trigger: Snatched Release

# Join Notification Test
# Author: Kevin Ould

import sys
import json
import urllib.request, urllib.parse
from time import strftime

script, title, year, imdbid, resolution, kind, downloader, downloadid, indexer, info_link, conf_json = sys.argv

conf = json.loads(conf_json)

apikey = conf['apikey']

deviceid = conf['deviceid']

icon = conf['icon']

join_api = 'https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?'

message = 'Watcher Snatched {} - sent to {} on {}.'.format(title, downloader, strftime("%a, %b %d, at %I:%M%p"))

post_data = {'text': message, 'deviceId': deviceid, 'apikey': apikey, 'icon': icon}

requests.get(join_api, params=post_data)

url = (join_api) + 'icon=' + urllib.parse.quote(icon) + '&text=' + urllib.parse.quote(message) + '&deviceId='+ (deviceid) + '&apikey=' + (apikey)
urllib.request.urlopen(url)

