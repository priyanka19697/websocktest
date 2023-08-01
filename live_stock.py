import requests
from datetime import datetime

url = "https://alpha-vantage.p.rapidapi.com/query"

timestamp = datetime.now()

print(timestamp)

querystring = {"interval":"1min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"full"}

headers = {
	"X-RapidAPI-Key": "e2b46d24b2msh3da3abc9da6a3c5p1380b6jsn32b090fed49e",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
response_data = response.json()

meta_data = response_data.get('Meta Data', {})
interval = meta_data['4. Interval']
time_series_key = f'Time Series ({interval})'
time_series = response_data.get(time_series_key, [])

print(len(time_series))

print("=================================================================================")
print(time_series[0])
