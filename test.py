# Imports
import requests as req
from datetime import datetime
from pprint import pprint
import json

# Local Imports
from lib.api.binance.interface import Binance
from tests.battery import *


# Test
Binance().test_bulk_klines('ethbtc','1m')
# Binance().test_klines(
#     "ltcbtc",
#     "1m"
# )
exit()
with open("db/info/binance/exchange_info.json", "r") as exchange_info:
    test = json.load(exchange_info)


properties = [
    'symbol',
    'status',
    'baseAsset',
    'baseAssetPrecision',
    'quoteAsset',
    'quotePrecision',
    'quoteAssetPrecision'
]
asset_list = []
for asset in test['symbols']:
    current_asset = {}

    for prop in properties:
        current_asset[prop] = asset[prop]
    
    asset_list.append(current_asset)

for a in asset_list:
    print(a)
exit()
binance = Binance()

test_exact(
    True,
    Binance().is_connected,
    None,
    True
)

print(binance.server_status())