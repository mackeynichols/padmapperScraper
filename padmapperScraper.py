#! python3
# padmapperScraper.py - takes inputs, returns interesting posts on padmapper via email

# inputs:
# 1: neighborhood
# 2: # of bedrooms
# 3: keywords (parking, for example)
# 4: min square feet
# ?min price?

import sys
import requests
import json

# get xz_token and csrf from https://www.padmapper.com/api/t/1/bundle
r = requests.get('https://www.padmapper.com/api/t/1/bundle').text
r_json = json.loads(r)

xz_token = r_json['xz_token']
csrf = r_json['csrf']


# use above to make a request to https://www.padmapper.com/api/t/1/pins
# ... with above tokens and input variables

# sort returned apartments by price, if all else is equal

# email certain records with photos and links
