## RSI INDICADOR PARAMS
RSI_PERIOD = 14
RSI_OVERBOUGHT = 65
RSI_OVERSOLD = 40
## Simulated Wallet Params
WALLET_COIN = 0
WALLED_USDT = 50
## Order amount for bot trading
ORDER_AMOUT = 0.01 

# Binance Dataframe configurations
TIMESTAMP_TO_MS = 1000
TIMESTAMP_DATA_KEY_BINANCE = "E"
CANDLE_KEY_BINANCE = "k"
CLOSE_PRICE_KEY_BINANCE = "c"
CANDLE_CLOSED_KEY_BINANCE = "x"
CANDLE_TIMESTAMP_KEY_BINANCE = "t"

# Dict for the kline full description message
KLINE_DESCRIPTION_DICT= {
    "t": "Kline start time",
    "T": "Kline close time",
    "s": "Symbol",
    "i": "Interval",
    "f": "First trade ID",
    "L": "Last trade ID",
    "o": "Open price",
    "c": "Close price",
    "h": "High price",
    "l": "Low price",
    "v": "Base asset volume",
    "n": "Number of trades",
    "x": "closed_candlestick",#"Is this kline closed",
    "q": "Quote asset volume",
    "V": "Taker buy base asset volume",
    "Q": "Taker buy quote asset volume",
    "B": "Ignore",
  }
  
#Gets Kline/Candlestick Streams 1 minute
SOCKET_INTERVAL = "1m" # 1 minute interval
SOCKET_PAIR = "ethusdt" # ETHUSDT trading pair
SOCKET_INFO= "kline" #The Kline/Candlestick Stream push updates to the current klines/candlestick every second.

SOCKET = "wss://stream.binance.com:9443/ws/"+ SOCKET_PAIR+"@"+ SOCKET_INFO+"_"+ SOCKET_INTERVAL