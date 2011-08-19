#!/usr/bin/env python
#
# Copyright 2011  Vincent Batts, Vienna, VA, USA
# 
# See LICENSE
#

import sys, os

# Setup our path, if this is running from the src directory
fpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"lib")
if os.path.exists(fpath):
    sys.path.insert(0,fpath)

# Our local configuration handler
from pygtasks.config import pygconfig

# These are from the apiclient in samples/ of the google-api-python-client
import httplib2
import gflags

try:
    from apiclient.discovery import build
except:
    print "ERROR: google-api-python-client libraries are needed"
    print "ERROR: please visit http://code.google.com/p/google-api-python-client/"
    exit(2)

# a fucntion for the map()
def transText(i):
    return i[u'translatedText']

p_config = pygconfig()

service = build('translate', 'v2', 
        developerKey=p_config.api_get('developerKey'))

if len(sys.argv) > 1:
    args = sys.argv
    args.pop(0)
else:
    args = ['flower','car']

print "To transale: %s" % " ".join(args)

ret = service.translations().list(
        source='en',
        target='fr',
        q=args
        ).execute()

str =  " ".join(map(transText, ret[u'translations']))
print "Translated: %s" % str



