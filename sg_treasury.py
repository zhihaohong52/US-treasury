import requests

url = 'https://eservices.mas.gov.sg/api/action/datastore/search.json?resource_id=ec2cb157-d25f-4245-a547-dc036b321a09'

response = requests.get(url)

import pandas as pd

#call json_normalize to flatten json in ‘result’ field
sg_treasury = pd.json_normalize(response.json()['result'] ['records'])

# group by year
sg_treasury['year'] = pd.DatetimeIndex(sg_treasury['end_of_quarter']).year
sg_treasury = sg_treasury.groupby('year').sum()
sg_treasury = sg_treasury.drop(columns=['end_of_quarter', 'preliminary', 'timestamp'])

#write csv file
import os
os.makedirs('C:/Users/James/OneDrive - Nanyang Technological University/GitHub/US treasury', exist_ok=True)
sg_treasury.to_csv('C:/Users/James/OneDrive - Nanyang Technological University/GitHub/US treasury/sg_treasury.csv')