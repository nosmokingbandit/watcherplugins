# /usr/bin/python3
# Watcher Plugin to send Pushbullet Notifications
# Trigger: Post-processing Finished

import sys
import json
import urllib.parse
import urllib.request
from time import strftime

title = sys.argv[1]
new_file = sys.argv[6]
conf_json = sys.argv[10]

conf = json.loads(conf_json)
apikey = conf['apikey']

pushbullet_api = 'https://api.pushbullet.com/v2/pushes'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + apikey}

body = {'type': 'link',
        'title': 'Watcher Finished Processing {}'.format(title),
        'body': '{} finished processing on: <br/> {}'.format(title, strftime("%a, %b %d, at %I:%M%p"), new_file),
        }

if conf.get('Send to Device Identifier'):
    body['device_iden'] = conf['Send to Device Identifier']

if conf['channel']:
    body['channel_tag'] = conf['channel']

body = json.dumps(body).encode('utf-8')

request = urllib.request.Request(pushbullet_api, body, headers)

try:
    response = urllib.request.urlopen(request)
except Exception as e:
    print(str(e))
    sys.exit(1)

sys.exit(0)
