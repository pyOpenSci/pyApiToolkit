#!/bin/env python3
# -*- coding: utf-8 -*-

"""
https://github.com/urschrei/pyzotero
https://www.zotero.org/support/dev/client_coding/javascript_api
http://pyzotero.readthedocs.io/en/latest/
"""

import pyApiToolkit as at
import os
from pyzotero import zotero
import include

__author__ = "Stefan Kasberger"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__status__ = "Development" # 'Development', 'Production' or 'Prototype'

###    GLOBAL   ###

DELAY_TIME = 5 # in seconds
TS = at.get_timestring()
# TS = '2015-10-28-14-59'

###    FUNCTIONS   ###

###    MAIN   ###

if __name__ == "__main__":
	startTime = at.start_timer()

	rootFolder = at.get_root_folder()
	config = include.data['zotero']
	at.setup_environment()
	data = {}

	# zotero API
	library_type = 'user'
	#library_type = 'group'
	zot = zotero.Zotero(config['zoteroID'], library_type, config['apiKey'])
	items = zot.top(limit=5)

	for item in items:
	    print(item['data'])
	
	at.stop_timer(startTime)
