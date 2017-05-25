#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests	
import pyApiToolkit as at

__author__ = "Stefan Kasberger"
__copyright__ = "Copyright 2017"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__status__ = "Development" # 'Development', 'Production' or 'Prototype'

###    GLOBAL   ###

BASE_URL = 'http://pub.orcid.org/'
API_VERSION = 'v1.1/'

# make request to DKAN API
def request_api(query, datatype):
	"""
	"""
	if datatype == 'json':
		acceptkey = 'application/orcid+json' # header: "Accept: application/orcid+json"
	elif datatype == 'html':
		acceptkey = 'text/html' # header: "Accept: text/html"
	else:
		acceptkey = 'application/orcid+xml' # header: "Accept: application/orcid+xml"
	
	headers = {'Accept': acceptkey}

	resp = requests.get(query, headers=headers)

	if resp.status_code != 200:
		# This means something went wrong.
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))

	return resp.text
	
# get all public fields from the bio
def get_orcidId(orcidId, datatype):
	"""
	Returns the fields set as "Public" in the bio portion of the ORCID Record 
	for the scholar represented by the specified orcidId. When used with an 
	access token and the Member API, limited-access data is also returned.
	http://pub.orcid.org/v1.1/0000-0001-7857-2795
	"""
	return request_api(BASE_URL+API_VERSION+orcidId, datatype)

# get all public fields from the bio
def get_works(orcidId, datatype):
	"""
	Returns the "works" research activities that are set as "Public" in the 
	ORCID Record for the scholar represented by the specified orcidId. When 
	used with an access token and the Member API, limited-access "works" are 
	also returned.
	http://pub.orcid.org/v1.1/0000-0001-7857-2795/orcid-works
	"""
	return request_api(BASE_URL+API_VERSION+orcidId+'/orcid-works', datatype)

# get all public fields from the bio
def get_profile(orcidId, datatype):
	"""
	Returns the fields set as "Public" in the bio portion of the ORCID Record 
	for the scholar represented by the specified orcidId. When used with an 
	access token and the Member API, limited-access data is also returned.
	http://pub.orcid.org/v1.1/0000-0001-7857-2795/orcid-profile
	"""
	return request_api(BASE_URL+API_VERSION+orcidId+'/orcid-profile', datatype)

def request_ids(orcidIds):
	for id in orcidIds:
		data[id] = get_profile(id, datatype)
	return data

def save_to_file(data, datatype):
	if datatype	== 'xml':
		for id in data:
			at.save_to_file(data[id], rootFolder+'/data/raw/xml/orcid_'+id+'.xml')

# main
if __name__ == '__main__':
	startTime = at.start_timer()
	data = {}
	rootFolder = at.get_root_folder()
	datatype = 'xml'
	baseUrl = 'http://pub.orcid.org/'
	at.setup_environment()

	df = at.open_csv(rootFolder+'/data/raw/csv/orcid.csv')

	#read_csv
	data = request_ids(df['orcid_id'])

	save_to_file(data, datatype)

	at.stop_timer(startTime)
