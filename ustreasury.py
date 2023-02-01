#import libraries
import pandas as pd
import io
import requests as requests

#set url to download csv file
URL = 'https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=bf17364827e38702b42a58cf8eaa3f78&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package'

#download csv file and read it into a pandas dataframe
response = requests.get(URL)
if response.status_code == 200:
    csvtext = response.text
    csvbuffer = io.StringIO(csvtext)
    us_treasury = pd.read_csv(csvbuffer)


#data cleaning
us_treasury = us_treasury.drop([0,1,2,3,4])
us_treasury.rename(columns={'Series Description':'Date'}, inplace=True)
us_treasury.set_index('Date', inplace=True)
us_treasury.replace(to_replace='ND', value='NaN', inplace=True)

for col in us_treasury.columns:
    us_treasury[col] = pd.to_numeric(us_treasury[col], errors='coerce')

#write csv file
import os
os.makedirs('C:/Users/James/OneDrive - Nanyang Technological University/GitHub/US treasury', exist_ok=True)  
us_treasury.to_csv('C:/Users/James/OneDrive - Nanyang Technological University/GitHub/US treasury/us_treasury.csv')