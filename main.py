import datetime
import time
from plyer import notification
import yfinance as yf
msft = yf.Ticker("MSFT")
data=msft.info


while True:
    notification.notify(
        title=f"MSFT data {datetime.date.today()}",
        message=f"Current Price: {data['currentPrice']}\nDay Low: {data['regularMarketDayLow']}\nDay High: {data['regularMarketDayHigh']}",
        timeout=10
    )
    time.sleep(60)  # notification every minute
