
from urllib.request import urlopen
import json
import os


def get_state_stations(url, state):
    print("Extracting data for %s stations" % state)
    json_data = urlopen(url).read()
    state_data = json.loads(json_data.decode('utf-8'))
    pretty_data = json.dumps(state_data, sort_keys=True, indent=4,separators=(',',':'))

    stations = {}
    for station in state_data['value']['timeSeries']:
        number = station['sourceInfo']['siteCode'][0]['value']
        code = int(number[0:2])
        if code < 16:
            stations[station['sourceInfo']['siteCode'][0]['value']] = {
                'name': station['sourceInfo']['siteName'],
                'number': station['sourceInfo']['siteCode'][0]['value'],
                'latitude': station['sourceInfo']['geoLocation']['geogLocation']['latitude'],
                'longitude': station['sourceInfo']['geoLocation']['geogLocation']['longitude']
               }
        else:
            pass
    filename = "stations/united_states/%s/stations.json" % (state)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    state_wa = open(filename,'w')
    state_wa.write(json.dumps(stations, sort_keys=True, indent=4, separators=(',',':')))
    state_wa.close()


states = {'AL': 'al',
          'AK': 'ak',
          'AZ': 'az',
          'AR': 'ar',
          'CA': 'ca',
          'CO': 'co',
          'CT': 'ct',
          'DE': 'de',
          'DC': 'dc',
          'FL': 'fl',
          'GA': 'ga',
          'HI': 'hi',
          'ID': 'id',
          'IL': 'il',
          'IN': 'in',
          'IA': 'ia',
          'KS': 'ks',
          'KY': 'ky',
          'LA': 'la',
          'ME': 'me',
          'MD': 'md',
          'MA': 'ma',
          'MI': 'mi',
          'MN': 'mn',
          'MS': 'ms',
          'MO': 'mo',
          'MT': 'mt',
          'NE': 'ne',
          'NV': 'nv',
          'NH': 'nh',
          'NJ': 'nj',
          'NM': 'nm',
          'NY': 'ny',
          'NC': 'nc',
          'ND': 'nd',
          'OH': 'oh',
          'OK': 'ok',
          'OR': 'or',
          'PA': 'pa',
          'RI': 'ri',
          'SC': 'sc',
          'SD': 'sd',
          'TN': 'tn',
          'TX': 'tx',
          'UT': 'ut',
          'VT': 'vt',
          'VA': 'va',
          'WA': 'wa',
          'WV': 'wv',
          'WI': 'wi',
          'WY': 'wy'
          }

for state in states.keys():
    url = "http://waterservices.usgs.gov/nwis/iv?format=json&stateCd={0}".format(state)
    get_state_stations(url, state)
