# Watcher Plugin to send Pushbullet Notifications
# Trigger: Post-processing Finished

import sys
import json
import urllib2
from time import strftime

title = sys.argv[1]
new_file = sys.argv[6]
conf_json = sys.argv[9]

conf = json.loads(conf_json)
apikey = conf['Api Key']

pushbullet_api = 'https://api.pushbullet.com/v2/pushes'
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + apikey}

body = {'type': 'link',
        'title': 'Watcher Finished Processing {}'.format(title),
        'body': '{} finished processing on: <br/> {}'.format(title, strftime("%a, %b %d, at %I:%M%p"), new_file_location),
        }

if conf.get('Send to Device Identifier'):
    body['device_iden'] = conf['Send to Device Identifier']

if conf['Send Using Channel']:
    body['channel_tag'] = conf['Send Using Channel']

body = json.dumps(body)

request = urllib2.Request(pushbullet_api, body, headers)

try:
    response = urllib2.urlopen(request)
except Exception, e:
    print str(e)
    sys.exit(1)

sys.exit(0)
