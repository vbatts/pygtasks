#
# Copyright 2011  Vincent Batts, Vienna, VA, USA
# 
# See LICENSE
#

import os, sys
import ConfigParser
DEFAULT = {
        'name': 'pygtask.cfg',
        'path': os.path.join(os.getenv('HOME'),'.config/pygtask'),
        'config': {
            'api': {
                'client_id': 'YOUR_CLIENT_ID',
                'client_secret': 'YOUR_CLIENT_SECRET',
                'user_agent': 'pygtasks/1.0',
                'developerKey': 'YOUR_DEVELOPER_KEY'
                },
            'client': {
                'storage_file': 'store.dat'
                }
            }
        }


def makeNewConfig( file = os.path.join(DEFAULT['path'], DEFAULT['name']) ):
    if not(os.path.exists(DEFAULT['path'])):
        os.makedirs(DEFAULT['path'])
    elif os.path.exists(file):
        sys.stderr.write("WARNING: %s already exists! please move it first"
                % file)
        return False


    f_new = open(file, 'wb')
    
    for section in DEFAULT['config'].keys():
        ## FIXME 
        # f_new.write(blah + '\n')
        for key in DEFAULT['config'][section]:
            ## FIXME 
            # f_new.write(blah + '\n')
            None
        
    f_new.close()

    return True
        

def showApiHelp(file = os.path.join(DEFAULT['path'], DEFAULT['name']) ):
    sys.stderr.write('''
INFO: Before pygtasks can operate, the client id and secret must
INFO: registered as an application. Please see the Google APIs console
INFO: and register a new 'project'
INFO: https://code.google.com/apis/console/
INFO: 
INFO: After that, update the information stored in %s
''' % file)
    return None



class pygconfig(object):
    
    def __init__(self, file = os.path.join(DEFAULT['path'], DEFAULT['name']) ):
        self.configp = ConfigParser.ConfigParser()

        if not(os.path.exists(file)):
            if makeNewConfig(file):
                showApiHelp(file)




