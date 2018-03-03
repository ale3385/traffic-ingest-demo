#Main ingestion script for accessing this dataset via the Socrata Open Data API

from __future__ import print_function, absolute_import
import pandas as pd
from sodapy import Socrata
from google.datalab import Context
import time
from datetime import datetime, timedelta
import logging

#Error logging
logging.basicConfig(level=logging.INFO)

#Authentication with Socrata Open Data API
#from sodapy import Socrata (https://github.com/xmunoz/sodapy)
# e.g. client = Socrata("sandbox.demo.socrata.com", "FakeAppToken", username="fakeuser@somedomain.com", password="ndKS92mS01msjJKs")
#Note: username and password are only required for creating or modifying data. 
#An application token isn't strictly required (can be None), but queries executed from a client without an application token will be subjected to strict throttling limits.

def run()
#Using Application Token generated
	client = Socrata("data.cityofchicago.org", "R2x0NehIGA6vUXE9WfUx2DOSV")
	                 
	# First 5000 results returned as JSON from API
	results = client.get("8v9j-bter", limit=5000)
	
	# Convert dataframe
	results_df = pd.DataFrame.from_records(results)	
	
	#sending to bigquery
	results_df.to_gbq('traffic-ingest-demo.chicago_traffic_data', "gcp-traffic-demo", chunksize=5000, verbose=True, if_exists='append')
