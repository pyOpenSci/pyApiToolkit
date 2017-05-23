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

def request_dois(dois):
	data = {}

	for doi in dois:
		data[doi] = sm.request_query(baseUrl+doi+'?email='+config['email'])
	return data

def save_to_files(data, rootFolder):
	i = 0
	for id in data:
		sm.save_to_json(data[id], rootFolder+'/data/raw/json/oadoi_'+str(i)+'.json')
		i+=1

###    MAIN   ###

if __name__ == "__main__":
	startTime = sm.start_timer()

	rootFolder = sm.get_root_folder()
	baseUrl = 'https://api.oadoi.org/'
	config = include.data['oadoi']
	sm.setup_environment()

	df = sm.open_csv(rootFolder+'/data/raw/csv/oadoi.csv')
	
	# oadoi API
	data = request_dois(df['doi'])

	save_to_files(data, rootFolder)
	
	sm.stop_timer(startTime)
