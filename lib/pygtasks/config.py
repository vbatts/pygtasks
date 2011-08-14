#
# Copyright 2011  Vincent Batts, Vienna, VA, USA
# 
# See LICENSE
#

import os, sys
import ConfigParser

DEFAULT = {
        'name': 'pygtasks.cfg',
        'path': os.path.join(os.getenv('HOME'),'.config/pygtasks'),
        'config': {
            'api': {
                'client_id': 'YOUR_CLIENT_ID',
                'client_secret': 'YOUR_CLIENT_SECRET',
                'user_agent': 'pygtasks/1.0',
                'developerKey': 'YOUR_DEVELOPER_KEY'
                },
            'client': {
                'storage_file': 'tasks.dat',
                'auth_local_webserver': 'False'
                }
            }
        }
    

class pygconfig(object):
    
    def __init__(self, cfg_file = os.path.join(DEFAULT['path'], DEFAULT['name']) ):
        self.configp = ConfigParser.ConfigParser()

        if not(os.path.exists(cfg_file)):
            if self.__makeNewConfig(cfg_file):
                self.__showApiHelp(cfg_file)
        else:
            ## TODO maybe do a simple check ?
            None

        ## TODO or maybe have a hash that is used in the interpolation ?
        self.configp.read(cfg_file)

    def get(self, section, key):
        try:
            return self.configp.get(section, key)
        except ConfigParser.NoOptionError:
            return False
        except ConfigParser.NoSectionError:
            return False

    def api_get(self, key):
        return self.get("api", key)

    def client_get(self, key):
        return self.get("client", key)

    
    def __makeNewConfig(self, file = os.path.join(DEFAULT['path'], DEFAULT['name']) ):
        cp = ConfigParser.ConfigParser()
    
        if not(os.path.exists(DEFAULT['path'])):
            os.makedirs(DEFAULT['path'])
        elif os.path.exists(file):
            sys.stderr.write("WARNING: %s already exists! please move it first"
                    % file)
            return False
        
        # Build up the configuration file from DEFAULT
        for section in DEFAULT['config'].keys():
            cp.add_section(section)
            for key in DEFAULT['config'][section]:
                cp.set(section, key, DEFAULT['config'][section][key])
            
        with open(file, 'wb') as configfile:
            cp.write(configfile)
    
        return True
            
    
    def __showApiHelp(self, file = os.path.join(DEFAULT['path'], DEFAULT['name']) ):
        sys.stderr.write('''
INFO: Before pygtasks can operate, the client id and secret must
INFO: registered as an application. Please see the Google APIs console
INFO: and register a new 'project'
INFO: https://code.google.com/apis/console/
INFO: 
INFO: P.S. the "developerKey", is the "API key" from the Google API console
INFO: 
INFO: After that, update the information stored in %s
''' % file)
        return None
    




