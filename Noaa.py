from noaa_sdk import noaa
import numpy as np
import pandas as pd
from matplotlib import pyplot


n = noaa.NOAA()

zipcodes = [31905, 11102, 19403, 10996]
cities = [
	{ 'zip': 31905, 'name': 'Fort Benning' },
	{ 'zip': 11102, 'name': 'Astoria' },
	{ 'zip': 19403, 'name': 'Norristown' },
	{ 'zip': 10996, 'name': 'West Point' }
]

d = {}
series = []
for city in cities:
	d = {}
	res = n.get_forecasts(city['zip'], 'US', True)

	print (city['name'] + '\n')
	for i in res:
		print(i['startTime'] + ': ' + str(i['temperature']) + i['temperatureUnit'])
		d[i['startTime']] = i['temperature']

	series.append(pd.Series(d))

for s in series:
	fig = pyplot.figure()
	s.plot()
	fig.savefig('figure1.png')
	pyplot.show()
    