#
# Copyright 2011  Vincent Batts, Vienna, VA, USA
# All rights reserved.
#
# Redistribution and use of this script, with or without modification, is
# permitted provided that the following conditions are met:
#
# 1. Redistributions of this script must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from pygtasks.pygconfig import pygconfig

# These are from the apiclient in samples/ of the google-api-python-client
import gflags
import httplib2

# Requires google-api-python-client
try:
    from apiclient.discovery import build
    from oauth2client.file import Storage
    from oauth2client.client import OAuth2WebServerFlow
    from oauth2client.tools import run
except:
    print "ERROR: google-api-python-client libraries are needed"
    print "ERROR: please visit http://code.google.com/p/google-api-python-client/"
    exit(2)

class pygservice(object):
    def __init__(self):
        # Setup the configuration getter
        self.p_config = pygconfig()
    

    def start(self):
        FLAGS = gflags.FLAGS
    
        # Set up a Flow object to be used if we need to authenticate. This
        # sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
        # the information it needs to authenticate. Note that it is called
        # the Web Server Flow, but it can also handle the flow for native
        # applications
        # The client_id and client_secret are copied from the API Access tab on
        # the Google APIs Console
        FLOW = OAuth2WebServerFlow(
            client_id = self.p_config.api_get('client_id'),
            client_secret = self.p_config.api_get('client_secret'),
            scope='https://www.googleapis.com/auth/tasks',
            user_agent= self.p_config.api_get('user_agent'))
        
        # To disable the local server feature, uncomment the following line:
        FLAGS.auth_local_webserver = self.p_config.configp.getboolean('client','auth_local_webserver')
        
        # If the Credentials don't exist or are invalid, run through the native client
        # flow. The Storage object will ensure that if successful the good
        # Credentials will get written back to a file.
        storage = Storage(self.p_config.client_get('storage_file'))
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
            developerKey = self.p_config.api_get('developerKey'))
        
        return service



