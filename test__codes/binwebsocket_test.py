from src.binbinance.BinWebSocket import BinWebSocket

#Gets Kline/Candlestick Streams 1 minute
SOCKET_INTERVAL = "1m" # 1 minute interval
SOCKET_PAIR = "ethusdt" # ETHUSDT trading pair
SOCKET_INFO= "kline" #The Kline/Candlestick Stream push updates to the current klines/candlestick every second.
SOCKET = "wss://stream.binance.com:9443/ws/"+ SOCKET_PAIR+"@"+ SOCKET_INFO+"_"+ SOCKET_INTERVAL

if __name__ == "__main__":
  ws = BinWebSocket(SOCKET)

  print("Starting operation with the following balances:")
  ws.binSim.printWalletBalance()
  
  ### Running Operation
  ws.update() 

  print("FINAL WALLET BALANCE")
  ws.binSim.printWalletBalance()
