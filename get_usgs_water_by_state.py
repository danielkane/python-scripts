import urllib, json

# This script extracts the most recent water data by state for all active sites in the USGS database.
# replace CA in stateCd=CA with the state you want to extract water data from

def write_usgs_water_to_file(state="CA"):
    url = 'http://waterservices.usgs.gov/nwis/iv/?format=json&stateCd={0}&modifiedSince=PT30M'.format(state)
    response = urllib.urlopen(url)
    parsed = json.loads(response.read())
    data = json.dumps(parsed, indent=4, sort_keys=True)

    data = str(data)
    f = open('usgs_sites_{0}.json'.format(state.lower()), 'w')
    f.write(data)
    f.close()
