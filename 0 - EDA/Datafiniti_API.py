#pip3 install requests

# Illustrates an API call to Datafiniti's Product Database for hotels.
import requests
import urllib.parse
import json

List=['''McDonald's''','Subway', 'Starbucks', 'KFC', 'Burger King', 'Pizza Hut', '''Domino's''', 'Dunkin Donuts', '''Wendy’s''', 'Chipotle Mexican Grill', 'Panera Bread', 'Five Guys', 'Shake Shack']

keyFile = open('/Users/c32/Documents/NYCDSA/Projects/2 R Data Analysis/Fast-Food/EDA/API_key', 'r')
key = keyFile.readline()
keyFile.close()

# Set your API parameters here.
API_token = key
format = 'JSON'
query = 'country:US'
num_records = 1
download = False

request_headers = {
	'Authorization': 'Bearer ' + API_token,
	'Content-Type': 'application/json',
}
request_data = { 
	"query": "dateUpdated:[2018-04-01 TO *] AND categories:\"Fast Food\" AND country:US* AND name:\"McDonald's\",
	"format": "csv", 
	"download": True
	}

#request_data = {
#    'query': query,
#    'format': format,
#    'num_records': num_records,
#    'download': download
#}

# Make the API call.
r = requests.post('https://api.datafiniti.co/v4/properties/search',json=request_data,headers=request_headers);

# Do something with the response.
if r.status_code == 200:
	print(r.content)
else:
	print('Request failed')