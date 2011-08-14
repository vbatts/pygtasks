"""
pygtasks 

A python Google tasks client

"""

__author__ = "Vincent Batts <vbatts@hashbangbash.com>"
__copyright__ = "Copyright 2011  Vincent Batts, Vienna, VA, USA"
__contributors = []
__license__ = "MIT"


try:
    from pygtasks.config import pygconfig
except ImportError: 
    pygconfig = None

try:
    from pygtasks.client import pygclient
except ImportError: 
    pygclient = None


