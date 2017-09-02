# /usr/bin/python3
# Watcher Plugin to trigger Plex Scanner for movie path
# Trigger: Post-processing Finished

import sys, json, os
from urllib.request import urlopen, Request
script, title, year, imdbid, resolution, kind, downloaddir, movedir, size, downloaddate, qualityprofile, conf_json = sys.argv

conf = json.loads(conf_json)

http = conf['HTTP']
host = conf['PLEX_HOST']
key = conf['MOVIE_SECTION_ID']
token = conf['PLEX_TOKEN']

url = "{0}://{1}/library/sections/{2}/refresh?X-Plex-Token={3}".format(http,host,key,token)

try:
     urlopen(url)
except Exception as e:
    print(str(e))
    sys.exit(1)

sys.exit(0)

