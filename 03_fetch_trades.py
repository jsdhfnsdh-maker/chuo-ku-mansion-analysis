import os
import requests
import pandas as pd

URL = "https://www.reinfolib.mlit.go.jp/ex-api/external/XIT001"


def fetch_trades(year, city="13102"): #cityのデフォルト値は中央区
    api_key = os.environ["REINFOLIB_API_KEY"]
    params = {"year": str(year),
          "city":"13102",
          "priceClassification":"01"}                    
    headers = {"Ocp-Apim-Subscription-Key": api_key}

    res = requests.get(URL, params=params, headers=headers)
    res.raise_for_status()
    return pd.DataFrame(res.json()["data"])


if __name__ == "__main__":
    df = fetch_trades(2015)
    print(df.shape)
    df.to_csv("raw_trades.csv", index=False, encoding="utf-8-sig")
