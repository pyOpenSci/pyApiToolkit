#!/bin/env python3
# -*- coding: utf-8 -*-

"""
Documentation: https://oadoi.org/api
"""

import scholmine as sm
import os
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
TS = sm.get_timestring()
# TS = '2015-10-28-14-59'

###    FUNCTIONS   ###

###    MAIN   ###

if __name__ == "__main__":
	rootFolder = sm.get_root_folder()

	config = include.data['oadoi']
	
	sm.setup_environment()
	startTime = sm.start_timer()

	# oadoi API
	baseUrl = 'https://api.oadoi.org/'
	doi = '10.1038/nature12873'

	data = sm.request_query(baseUrl+doi+'?email='+config['email'])

	print(data)

	sm.save_to_json(data, rootFolder+'/data/raw/json/oadoi.json')
	
	sm.stop_timer(startTime)
