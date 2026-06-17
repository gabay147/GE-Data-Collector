"""
This script allows the user to pull [TIMESPAN] of data from the OSRS
Wiki Grand Exchange API, available at:
https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices

Code version 0.0.1 by github.com/gabay147
"""

# Install packages
import requests

# Set credentials
headers = {
    'User-Agent':'GE Data Collector by @_deja.vu on Discord',
}

base_target = "https://prices.runescape.wiki/api/v1/osrs"

# Try getting base_target + /mapping
req = requests.get(base_target + '/mapping', headers=headers)

print(req.status_code)
print(req.text)
data = req.json()
print(data)
# response = requests.get(url, headers=headers)

# BEGIN SCRAPING CODE