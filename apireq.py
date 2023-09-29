import requests
import pandas as pd

url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(url)

if response.status_code == 200:
    info = response.json()
    df = pd.DataFrame(info)
    df.to_csv("binance_24hr_ticker_data.csv", index=False)
    print("CSV file saved successfully.")
else:
    print("Request failed - status code: ", response.status_code)

