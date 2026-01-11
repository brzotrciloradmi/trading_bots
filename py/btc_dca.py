
from keys import api_key, full_priv_key

#CryptoCurrency eXchange Trading Library
import ccxt

# timer dependency
import time

# Logging
import logging
from logging.handlers import RotatingFileHandler

from telegram_bot import telegram_notifier as notifier

logger = logging.getLogger("dca_logger")
logger.setLevel(logging.INFO)

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': full_priv_key,
    "enableRateLimit": True,   # avoid bans / 429s
})

# symbol: 'BTC/USDT', 'buy', 0.0001)
def place_order(symbol, side, amount):
    order = exchange.create_market_order(symbol, side, amount)

if __name__=="__main__":
    SECONDS_24H = 24 * 60 * 60
    buyAmountUSDT = 30
    SYMBOL = 'BTC/USDT'

    while(True):
        # Trading Stragegy - DCA
        time.sleep(SECONDS_24H)
        orderAmount = exchange.amount_to_precision(SYMBOL, buyAmountUSDT)

        notifier.notify("Executing BTC DCA buy for " + buyAmountUSDT + "USDT")
        # Execution
        order = place_order(SYMBOL, 'buy', orderAmount)
        # logger.info('BTC DCA order executed for ' + buyAmountUSDT + 'USDT')

