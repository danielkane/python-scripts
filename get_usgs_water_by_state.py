import urllib, json

# This script extracts the most recent water data by state for all active sites in the USGS database.
# replace CA in stateCd=CA with the state you want to extract water data from

response = urllib.urlopen('http://waterservices.usgs.gov/nwis/iv/?format=json&stateCd=CA&modifiedSince=PT30M')
parsed = json.loads(response.read())
data = json.dumps(parsed, indent=4, sort_keys=True)


data = str(data)
f = open('usgs_sites_ca.json', 'w')
f.write(data)
f.close()
