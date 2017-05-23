#!/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import requests	
import json
import os
import csv
import sqlite3
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


def get_root_folder():
	return os.path.dirname(os.getcwd())

def setup_environment():
	"""Sets up the folder structure and working environment.
	"""
	rootFolder = get_root_folder()
	folderRawJSON = rootFolder + '/data/raw/json/'
	folderRawXML = rootFolder + '/data/raw/xml/'
	folderRawCSV = rootFolder + '/data/raw/csv/'
	folderSQLite3 = rootFolder + '/data/sqlite3/'
	if not os.path.exists(folderRawCSV):
		os.makedirs(folderRawCSV)
	if not os.path.exists(folderRawJSON):
		os.makedirs(folderRawJSON)
	if not os.path.exists(folderRawXML):
		os.makedirs(folderRawXML)
	if not os.path.exists(folderSQLite3):
		os.makedirs(folderSQLite3)

def get_timestring():
	return datetime.now().strftime('%Y-%m-%d-%H-%M')

def save_to_file(data, filename):
	"""Saves file on specified place on harddrive.
	
	Args:
		data: string to save.
		filename: string of the filepath.
	"""
	try:
		f = open('filename', 'w')
		text_file = open(filename, "w")
		text_file.write(data)
		text_file.close()
	except:
		print('Error writing', filename)
		return False


def save_to_json(data, filename):
	try:
		data = json.dumps(data, indent=2, sort_keys=True)
	except:
		print('Error opening', filename)
		return None
	save_to_file(data, filename)

def read_file(filename):
	"""Reads file and returns the text.
	
	Args:
		filename: name of the file
	
	Returns:
		string: content of file as string
	"""
	f = open(filename, 'w')
	string = f.read()

	return string

def create_sqlite3_db(filename):
	return sqlite3.connect(filename)

def execute_sqlite3_query(query):
	c = conn.cursor()
	c.execute(query)

def commit_sqlite3(conn):
	conn.commit()

def close_sqlite3_conn(conn):
	conn.close()

def start_timer():
	startTime = datetime.now()
	print('start:', startTime)
	return startTime	

def stop_timer(startTime):
	print('runtime:', (datetime.now() - startTime))

def request_query(query):
	resp = requests.get(query)

	if resp.status_code != 200:
		# This means something went wrong.
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))

	return resp.json()

def read_csv(filename, delimiter=',', newline='', quotechar='"'):
	data = csv.DictReader(open(filename, newline=newline), delimiter=delimiter, quotechar=quotechar)
	return data

# sqlalchemy http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
# http://docs.sqlalchemy.org/en/rel_1_1/









