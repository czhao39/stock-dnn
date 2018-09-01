import requests
import secret

import io
import pandas as pd


AV_ENDPOINT = "https://www.alphavantage.co/query"


def get_time_series_daily_adjusted(sym: str):
    return pd.read_csv(io.StringIO(requests.get(AV_ENDPOINT, params={
        "apikey": secret.AV_API_KEY,
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": sym,
        "outputsize": "full",
        "datatype": "csv"
    }).text))


if __name__ == "__main__":
    print(get_time_series_daily_adjusted("msft").head(20))
