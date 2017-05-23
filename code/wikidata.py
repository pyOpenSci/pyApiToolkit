#!/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import scholmine as sm
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
TS = sm.get_timestring()
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

###    MAIN   ###

if __name__ == "__main__":
	rootFolder = sm.get_root_folder()

	config = include.data['wikidata']
	sm.setup_environment()
	startTime = sm.start_timer()

	# wikidata API
	login(config['user'], config['password'])
	item = 'Q5'
	results = query_item(item)
	data = get_data(results)

	sm.save_to_json(data, rootFolder+'/data/raw/json/wikidata.json')

	#sm.create_sqlite3_db(rootFolder+'/data/sqlite3/wikidata.db')

	sm.stop_timer(startTime)
