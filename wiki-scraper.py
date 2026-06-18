"""
This script allows the user to pull [TIMESPAN] of data from the OSRS
Wiki Grand Exchange API, available at:
https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices

Code version 0.0.1 by github.com/gabay147
"""

# Install packages
import requests
import pandas as pd
from pathlib import Path
import json

# Set credentials
# OSRS Wiki prefers [feature] by [username] format
headers = {
    'User-Agent':'GE Data Collector by @_deja.vu on Discord',
}

# BASE TARGET
# The base address for the API
base_target = "https://prices.runescape.wiki/api/v1/osrs"

# CACHE FILES
CACHE_MAPPING = Path('cache/ge_mapping.json')
CACHE_TIMESERIES = Path('cache/ge_timeseries.json')

# get_mapping
"""Get GE mapping
Gets mapping data from API if cached version does not exist

This function checks for an existing cached version of the data (as
ge_mapping.json) and returns the json data. If the cached file does not
exist, it will write the cache file instead.
"""
def get_mapping():
    if CACHE_MAPPING.exists():
        with open(CACHE_MAPPING, 'r') as f:
            print('Using cached mapping')
            return json.load(f)

    data = requests.get(base_target + '/mapping', headers=headers).json()

    with open(CACHE_MAPPING, 'w') as f:
        json.dump(data, f)

    print('Pulling mapping from API')
    return data

mapping = get_mapping()
print(mapping[:5])

# BEGIN SCRAPING CODE