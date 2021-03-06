"""
pygtasks 

A python Google tasks client

"""

__author__ = "Vincent Batts <vbatts@hashbangbash.com>"
__copyright__ = "Copyright 2011  Vincent Batts, Vienna, VA, USA"
__contributors = []
__license__ = "MIT"


try:
    from pygtasks.pygtask import pygtask
except ImportError: 
    pygtask = None

try:
    from pygtasks.pygconfig import pygconfig
except ImportError: 
    pygconfig = None

try:
    from pygtasks.pygservice import pygservice
except ImportError: 
    pygservice = None

try:
    from pygtasks.pygclient import pygclient
except ImportError: 
    pygclient = None


