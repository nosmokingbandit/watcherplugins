# /usr/bin/python3
# Watcher Plugin to send Pushbullet Notifications
# Trigger: Snatched Release

import sys
import json
import urllib.parse
import urllib.request
from time import strftime

script, title, year, imdbid, resolution, kind, downloader, downloadid, indexer, info_link, conf_json = sys.argv

conf = json.loads(conf_json)

apikey = conf['apikey']

pushbullet_api = 'https://api.pushbullet.com/v2/pushes'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + apikey}

body = {'type': 'link',
        'title': 'Watcher Snatched {}'.format(title),
        'body': '{} sent to {} on {}.'.format(title, downloader, strftime("%a, %b %d, at %I:%M%p")),
        'url': urllib.parse.unquote(info_link)
        }

if conf['channel'] != '':
    body['channel_tag'] = conf['channel']

body = json.dumps(body).encode('utf-8')

request = urllib.request.Request(pushbullet_api, body, headers)

try:
    response = urllib.request.urlopen(request)
except Exception as e:
    print(str(e))
    sys.exit(1)

sys.exit(0)
