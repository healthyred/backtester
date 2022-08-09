import cbpro
import os
from enum import Enum
from datetime import date, datetime, timedelta
from time import sleep
import pandas as pd

"""
File that includes APIs for backtesting a strategy.
"""

c = cbpro.PublicClient()

def format_datetime_for_cb(datetime: datetime):
    return f'{datetime.strftime("%Y")}-{datetime.strftime("%m")}-{datetime.strftime("%d")} {datetime.strftime("%H")}:{datetime.strftime("%M")}:00.000'

def get_pnl_for_range(
    asset, 
    start_date: datetime, 
    end_date: datetime, 
    seconds_frame = 15*60,
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

    # 2022-Aug-08 18:19:00.000
    start = format_datetime_for_cb(start_date)
    ending = format_datetime_for_cb(start_date + timedelta(minutes=5))
    start_results = c.get_product_historic_rates(
        product_id=asset,
        start=start,
        end=ending,
        granularity=seconds_frame)


    end_start = format_datetime_for_cb(end_date)
    ending_2 = format_datetime_for_cb(end_start + timedelta(minutes=5))

    end_results = c.get_product_historic_rates(
        product_id=asset,
        start=end_start,
        end = ending_2,
        granularity=seconds_frame)

    print(start_results)
    # TODO: error handling
    # start_price = start_results[0]
    print("end")
    print(end_results)

    # Get order book and find price impact

    # historical = pd.DataFrame(c.get_product_historic_rates(product_id='ETH-USD'))
    # historical.columns= ["Date","Open","High","Low","Close","Volume"]
    # historical['Date'] = pd.to_datetime(historical['Date'], unit='s')
    # historical.set_index('Date', inplace=True)
    # historical.sort_values(by='Date', ascending=True, inplace=True)
    # historical

    return

test1 = datetime.now() - timedelta(1)
test2 = test1 - timedelta(1) 
get_pnl_for_range('BTC-USD', test1, test2)