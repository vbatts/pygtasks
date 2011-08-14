#!/usr/bin/env python

import sys

import httplib2
import gflags

from apiclient.discovery import build

def transText(i):
    return i[u'translatedText']

service = build('translate', 'v2', 
        developerKey='AIzaSyCcyk3MXrc6F3He95D5tULGigJ06AYZA2w')

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



