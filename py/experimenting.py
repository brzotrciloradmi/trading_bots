import pandas as pd

from keys import full_priv_key, api_key

#CryptoCurrency eXchange Trading Library
import ccxt

# Technical Analysis lib
import ta

# timer dependency
import time

from telegram_bot import telegram_notifier as notifier

# binance specific lib
# from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

exchangePub = ccxt.binance({
    "enableRateLimit": True,
})

exchangePriv = ccxt.binance({
    'apiKey': api_key,
    'secret': full_priv_key,
    "enableRateLimit": True,   # avoid bans / 429s
})


# symbol: 'BTC/USDT', 'buy', 0.0001)
def place_order(symbol, side, amount):
    order = exchangePriv.create_market_order(symbol, side, amount)
    print(order)

def USDTtoBTC(inputUSDT, priceBTC_USDT):
    return inputUSDT/priceBTC_USDT



if __name__=="__main__":
    print("Start of program.")
    notifier.notify("Trading notifier started.")
    # Fetch last N 1-hour candles for BTC/USDT
    bars = exchangePub.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)
    # df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    # df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # print(df.tail())

    # boll = ta.volatility.BollingerBands(df['close'], 20, 2, False)
    # print(boll.bollinger_hbanfetch_ohlcvd())
    # print(boll.bollinger_lband())

    # print(boll.bollinger_hband_indicator())



    # sma = ta.trend.SMAIndicator(df['close'], window=20).sma_indicator()
