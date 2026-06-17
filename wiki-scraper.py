"""
This script allows the user to pull [TIMESPAN] of data from the OSRS
Wiki Grand Exchange API, available at:
https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices

Code version 0.0.1 by github.com/gabay147
"""

# Set credentials
headers = {
    'User-Agent':'GE Data Collector by @_deja.vu on Discord',
}

base_target = "prices.runescape.wiki/api/v1/osrs"
# response = requests.get(url, headers=headers)

# BEGIN SCRAPING CODE