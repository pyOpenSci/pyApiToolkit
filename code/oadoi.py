#!/bin/env python3
# -*- coding: utf-8 -*-

"""
Documentation: https://oadoi.org/api
"""

import pyApiToolkit as at
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
TS = at.get_timestring()
# TS = '2015-10-28-14-59'

###    FUNCTIONS   ###

def request_dois(dois):
	data = {}

	for doi in dois:
		data[doi] = at.request_query(baseUrl+doi+'?email='+config['email'])
	return data

def save_to_files(data, rootFolder):
	i = 0
	for id in data:
		at.save_to_json(data[id], rootFolder+'/data/raw/json/oadoi_'+str(i)+'.json')
		i+=1

###    MAIN   ###

if __name__ == "__main__":
	startTime = at.start_timer()

	rootFolder = at.get_root_folder()
	baseUrl = 'https://api.oadoi.org/'
	config = include.data['oadoi']
	at.setup_environment()

	df = at.open_csv(rootFolder+'/data/raw/csv/oadoi.csv')
	
	# oadoi API
	data = request_dois(df['doi'])

	save_to_files(data, rootFolder)
	
	at.stop_timer(startTime)
