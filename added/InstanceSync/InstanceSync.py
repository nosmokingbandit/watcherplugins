'''
This plugin will automatically add a movie to a second Watcher instance when called
'''

import sys
import json
from urllib.request import urlopen

script, title, year, imdbid, quality, config_json = sys.argv

print('Executing plugin {} for {}'.format(script, title))

conf = json.loads(config_json)

affected_qualities = [i.strip() for i in conf['affected_qualities'].split(',') if i != '']

if len(affected_qualities) > 0 and quality not in affected_qualities:
    print('Quality Profile "{}" not selected to sync.'.format(quality))
    sys.exit(0)

response = urlopen('{}:{}/api?apikey={}&mode=addmovie&imdbid={}&quality={}'.format(conf['remote_host'], conf['remote_port'], conf['remote_api'], imdbid, quality))


sys.exit(0)
