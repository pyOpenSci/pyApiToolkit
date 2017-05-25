#!/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import pyApiToolkit as at
import os
from wikidataintegrator import wdi_core, wdi_login
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

def login(user, password):
	login_instance = wdi_login.WDLogin(user=user, pwd=password)

def query_item(itemID):
	return wdi_core.WDItemEngine(wd_item_id=itemID)

def get_data(results):
	return results.get_wd_json_representation()

def write_item():
	# Search for and then edit/create new item
	wd_item = wdi_core.WDItemEngine(item_name='<your_item_name>', domain='genes', data=[entrez_gene_id])
	wd_item.write(login_instance)

def save_to_files(data, rootFolder):
	for item in data:
		at.save_to_json(data[item], rootFolder+'/data/raw/json/wikidata_'+item+'.json')

###    MAIN   ###

if __name__ == "__main__":
	startTime = at.start_timer()

	rootFolder = at.get_root_folder()
	config = include.data['wikidata']
	at.setup_environment()
	data = {}

	# wikidata API
	login(config['user'], config['password'])
	
	df = at.open_csv(rootFolder+'/data/raw/csv/wikidata.csv')

	for item in df['item']:
		results = query_item(item)
		data[item] = get_data(results)

	save_to_files(data, rootFolder)

	#at.create_sqlite3_db(rootFolder+'/data/sqlite3/wikidata.db')

	at.stop_timer(startTime)
