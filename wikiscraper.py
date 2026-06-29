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
from time import sleep

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

# DEFINE FUNCTIONS
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

    print('Pulling mapping from API')
    data = requests.get(base_target + '/mapping', headers=headers).json()

    with open(CACHE_MAPPING, 'w') as f:
        print('Writing cached mapping')
        json.dump(data, f)

    return data

# get_timeseries
"""

Required API arguments
id - (required) Item id to return a time-series for.
timestep - (required) Timestep of the time-series. Valid options are "5m", "1h", "6h" and "24h".
"""
def get_timeseries(item_id, timestep):
    params = {
        'id':item_id,
        'timestep':timestep,
    }

    print('retrieving timeseries for item {}'.format(item_id))
    data = requests.get(base_target + '/timeseries', headers=headers, params=params, timeout=10).json()

    return data

# get_data
"""
Pulls timeseries data for each item in enumerable item_ids
"""
def get_data(item_ids, timestep = '24h', ratelimit = 1):
    frames = []

    for item_id in item_ids:
        df = pd.json_normalize(
            get_timeseries(item_id, timestep)['data']
        )

        df['item_id'] = item_id
        frames.append(df)

        sleep(ratelimit)

    final_df = pd.concat(frames, ignore_index=True)
    return final_df


# # Get mapping
# mapping = get_mapping()
# print(mapping[:5])
#
# # TEST: Get timeseries data for first item in mapping
# # Get first item id in mapping
# first_id = mapping[1]['id']
# print(first_id)
#
# # Get first timeseries
# first_timeseries = get_timeseries(first_id, timestep="24h")
# print(first_timeseries)



# BEGIN SCRAPING CODE