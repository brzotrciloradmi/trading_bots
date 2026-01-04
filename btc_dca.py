
from keys import api_key, full_priv_key

#CryptoCurrency eXchange Trading Library
import ccxt

# timer dependency
import time


exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': full_priv_key,
    })

# symbol: 'BTC/USDT', 'buy', 0.0001)
def place_order(symbol, side, amount):
    order = exchange.create_market_order(symbol, side, amount)
    print(order)

# Convert USDT to Target Symbol value.
def convert(inputUSDT, targetSymbolPrice):
    return inputUSDT/targetSymbolPrice



if __name__=="__main__":
    SECONDS_24H = 24 * 60 * 60

    while(True):
        ticker = exchange.fetch_ticker("BTC/USDT")
        current_BTCUSDT_price = ticker['last']

        orderSize = convert(30, current_BTCUSDT_price)
        place_order('BTC/USDT', 'buy', orderSize)

        time.sleep(SECONDS_24H)


