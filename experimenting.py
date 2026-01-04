import pandas as pd

from keys import private_key, public_key, api_key

#CryptoCurrency eXchange Trading Library
import ccxt

# Technical Analysis lib
import ta

# timer dependency
import time

# binance specific lib
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

exchange = ccxt.binance({
    'apiKey': public_key,
    'secret': private_key
    })

# symbol: 'BTC/USDT', 'buy', 0.0001)
def place_order(symbol, side, amount):
    order = exchange.create_market_order(symbol, side, amount)
    print(order)

def USDTtoBTC(inputUSDT, priceBTC_USDT):
    return inputUSDT/priceBTC_USDT



if __name__=="__main__":
    # Fetch last N 1-hour candles for BTC/USDT
    # bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)
    # df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    # df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # print(df.tail())

    # boll = ta.volatility.BollingerBands(df['close'], 20, 2, False)
    # print(boll.bollinger_hbanfetch_ohlcvd())
    # print(boll.bollinger_lband())

    # print(boll.bollinger_hband_indicator())



    # sma = ta.trend.SMAIndicator(df['close'], window=20).sma_indicator()
