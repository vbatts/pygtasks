from distutils.core import setup
import sys

setup (name              = "pygtasks",
       version           = "0.9.0",
       description       = "pygtasks - A command line Python client for Google Tasks",
       maintainer        = "Vincent Batts",
       maintainer_email  = "vbatts@hashbangbash.com",
       license           = "MIT",
       long_description  = "pygtasks is a command line Python client for Google Tasks",
       url               = "http://github.com/vbatts/pygtasks",
       platforms         = ['Any'],
       packages          = ['pygtasks','httplib2'],
       py_modules        = ['gflags','gflags_validators'],
       scripts           = ['bin/pygtasks','bin/translate_text'],
       package_dir       = {'': 'lib/'},
       )

