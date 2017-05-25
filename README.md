# Python Open Science API toolkit
Python 3 scripts to access, create, distribute and publish open research data or data about open science works.

**Requirements**
- Pandas
- include.py: this is a config file, where you store your personal information in a dictionaries. See more details at the specific wrappers on how to use this.

## pyApiToolkit.py

Basic functionalities, which are used by the other scripts listed further below.

## Wrapper

### oadoi.py

Python wrapper to access the [oadoi.org API](https://oadoi.org/api).

**include.py**

´´´
data = {
	'oadoi': {
		'email': 'EMAIL'
	}
}
´´´

### wikidata.py
Python wrapper to access the [wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) API via the [wikidataintegrator](https://github.com/SuLab/WikidataIntegrator) module (must be installed to work).

You have to have a wikidata account for this.

**include.py**

´´´
data = {
	'wikidata': {
		'user': 'USERNAME',
		'password': 'PASSWORD'
	}
}
´´´

### orcid.py
Python wrapper to access the [ORCID](https://orcid.org/) API.

### zotero.py

Wrapper for the [Zotero API](https://www.zotero.org/support/dev/client_coding/javascript_api). Ìt uses the [pyZotero](https://github.com/urschrei/pyzotero) python module, which must be installed to work.

**include.py**

´´´
data = {
	'zotero': {
		'apiKey': 'API_KEY',
		'zoteroID': 'ZOTEROID'
	}
}
´´´

### doaj.py
Wrapper to access the [Digital Open Access Journal API](https://doaj.org/api/v1/docs).

