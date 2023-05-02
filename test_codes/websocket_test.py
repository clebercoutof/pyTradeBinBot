import websocket

def on_open(ws):
  print("open")

def on_close(ws):
  print("close")

def on_message(ws,message):
  print(message)
  print("mesasge")

#Gets Kline/Candlestick Streams 1 minute
SOCKET_INTERVAL = "1m" # 1 minute interval
SOCKET_PAIR = "ethusdt" # ETHUSDT trading pair
SOCKET_INFO= "kline" #The Kline/Candlestick Stream push updates to the current klines/candlestick every second.

SOCKET = "wss://stream.binance.com:9443/ws/"+ SOCKET_PAIR+"@"+ SOCKET_INFO+"_"+ SOCKET_INTERVAL
if __name__ == "__main__":
  print("GETTING DATA FROM WEBSOCKET: "+ SOCKET)

  ws = websocket.WebSocketApp(SOCKET,
                              on_open=on_open,
                              on_message=on_message, 
                              on_close=on_close)
  ws.run_forever()
