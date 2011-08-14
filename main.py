#!/usr/bin/env python
# pygtasks (Python Google Task client)
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
from pygtasks.client import pygclient

# These are from the apiclient in samples/ of the google-api-python-client
import gflags
import httplib2

try:
    from apiclient.discovery import build
    from oauth2client.file import Storage
    from oauth2client.client import OAuth2WebServerFlow
    from oauth2client.tools import run
except:
    print "ERROR: google-api-python-client libraries are needed"
    print "ERROR: please visit http://code.google.com/p/google-api-python-client/"
    exit(2)


p_config = pygconfig()


FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret are copied from the API Access tab on
# the Google APIs Console
FLOW = OAuth2WebServerFlow(
    client_id = p_config.api_get('client_id'),
    client_secret = p_config.api_get('client_secret'),
    scope='https://www.googleapis.com/auth/tasks',
    user_agent= p_config.api_get('user_agent'))

# To disable the local server feature, uncomment the following line:
FLAGS.auth_local_webserver = p_config.configp.getboolean('client','auth_local_webserver')

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage(p_config.client_get('storage_file'))
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
service = build(serviceName='tasks', version='v1', http=http,
       developerKey = p_config.api_get('developerKey'))



## Main

tasklists = service.tasklists().list().execute()

print "Task Lists:"
for tasklist in tasklists['items']:
    print tasklist['title']
    #for k in tasklist.keys():
    #    print "%s :: %s" % (k,tasklist[k])

print ""

tasks = service.tasks().list(tasklist='@default').execute()

print "Tasks:"
for task in tasks['items']:
      print task['title']


