import cbpro
import os
from enum import Enum
from datetime import date, datetime
from time import sleep
import pandas as pd

"""
File that includes APIs for backtesting a strategy.
"""

c = cbpro.PublicClient()

def get_pnl_for_range(
    asset, 
    start_date: datetime, 
    end_date: datetime, 
    seconds_frame = 10*60,
    default_size = 10000,
    side = "BUY",
    ):
    """
    @param asset: asset that we want to check
    @param start_date: the start date for the position
    @param end_date
    @param seconds_frame: the interval which the tick data is
    @param default_size: how much money
    @param side: BUY or SELL

    @return float for profit or loss based on coinbase api
    """

    start = f'{start_date.strftime("%Y")}-{start_date.strftime("%b")}-{start_date.strftime("%d")} {start_date.strftime("%H")}:{start_date.strftime("%m")}:00.000'
    end = f'{end_date.strftime("%Y")}-{end_date.strftime("%b")}-{end_date.strftime("%d")} {end_date.strftime("%H")}:{end_date.strftime("%m")}:00.000'

    start_results = c.get_product_historic_rates(
        product_id=asset,
        start=start,
        granularity=seconds_frame)

    end_results = c.get_product_historic_rates(
        product_id=asset,
        start=end,
        granularity=seconds_frame)

    # TODO: error handling
    start_price = start_results[0]

    # Get order book and find price impact

    # historical = pd.DataFrame(c.get_product_historic_rates(product_id='ETH-USD'))
    # historical.columns= ["Date","Open","High","Low","Close","Volume"]
    # historical['Date'] = pd.to_datetime(historical['Date'], unit='s')
    # historical.set_index('Date', inplace=True)
    # historical.sort_values(by='Date', ascending=True, inplace=True)
    # historical

    return
