#!/bin/env python3
# -*- coding: utf-8 -*-

"""
Documentation: https://doaj.org/api/v1/docs
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
BASE_URL = 'http://doaj.org/api/v1/'
# TS = '2015-10-28-14-59'

###    FUNCTIONS   ###

def search_journals(query):
	return sm.request_query(BASE_URL+'search/journals/'+query)

def search_articles(query):
	return sm.request_query(BASE_URL+'search/articles/'+query)

def retrieve_article(articleId):
	return sm.request_query(BASE_URL+'articles/'+articleId)

def retrieve_journal_by_id(journalId):
	return sm.request_query(BASE_URL+'journals/'+journalId)

###    MAIN   ###

if __name__ == "__main__":
	startTime = sm.start_timer()

	rootFolder = sm.get_root_folder()
	sm.setup_environment()

	
	# search articles
	#df = sm.open_csv(rootFolder+'/data/raw/csv/doaj_searcharticles.csv')
	query = 'libya'
	dataSA = search_articles(query)
	sm.save_to_json(dataSA, rootFolder+'/data/raw/json/doaj_searcharticles_'+query+'.json')

	# retrieve article
	#df = sm.open_csv(rootFolder+'/data/raw/csv/doaj_articles.csv')
	articleId = '000011857dbc42afb0f1a8c7e35ab46f'
	dataRA = retrieve_article(articleId)
	sm.save_to_json(dataRA, rootFolder+'/data/raw/json/doaj_retrievearticle_'+articleId+'.json')

	# search journals
	#df = sm.open_csv(rootFolder+'/data/raw/csv/doaj_searchjournals.csv')
	query = 'geography'
	dataSJ = search_journals(query)
	sm.save_to_json(dataSJ, rootFolder+'/data/raw/json/doaj_searchjournals_'+query+'.json')

	# retrieve journal by ID
	#df = sm.open_csv(rootFolder+'/data/raw/csv/doaj_journalID.csv')
	#journalId = '2503-250X'
	#dataRJ = retrieve_journal_by_id(journalId)
	#sm.save_to_json(dataRJ, rootFolder+'/data/raw/json/doaj_retrievejournal_'+journalId+'.json')

	sm.stop_timer(startTime)
