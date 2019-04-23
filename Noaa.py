from noaa_sdk import noaa
n = noaa.NOAA()

zipcodes = [31905, 11102, 19403, 10996]
cities = [
	{ 'zip': 31905, 'name': 'Fort Benning' },
	{ 'zip': 11102, 'name': 'Astoria' },
	{ 'zip': 19403, 'name': 'Norristown' },
	{ 'zip': 10996, 'name': 'West Point' }
]

for city in cities:
	res = n.get_forecasts(city['zip'], 'US', True)

	print (city['name'] + '\n')
	for i in res:
		print(i['startTime'] + ': ' + str(i['temperature']) + i['temperatureUnit'])
