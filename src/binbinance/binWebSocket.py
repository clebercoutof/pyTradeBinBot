from numpy import empty
import json,datetime
import websocket,numpy,talib
from .logManager import *
from .binOrderSim import *
from .binalytics import Binalytics
from .app_params import *

class BinWebSocket:
  """ Class used to operate binance togeter with python inside bintradebot"""
  def __init__(self,wsurl):
    self.wsurl = wsurl
    self.ws = websocket.WebSocketApp(wsurl,
                                    on_open=self.on_open,
                                    on_message=self.on_message,
                                    on_close=self.on_close)
    
    self.binSim = BinOrderSim(WALLET_COIN,WALLED_USDT)
    self.last_close_price = 0
    self.in_position = False

    self.closes = []
    self.binalytics = Binalytics()

    self.RSI_STARTED = False
    self.current_period = 0

  def on_open(self,ws):
    """Function triggered when websocket Opens

    Args:
        ws (_type_): _description_
    """
    print("Web Socket Open Success")

  def on_close(self,ws):
    """Function triggered when websocket closes

    Args:
        ws (websocket.WebSocketApp): WebSocketApp object reference  
    """
    print("Web Socket Close Success")

  def on_message(self,ws,message):
    """Function triggered when websockets receives a message

    Args:
        ws (websocket.WebSocketApp): WebSocketApp object reference 
        message (string): Received websocket message
    """
    # Reads message and converts to json 
    json_message = json.loads(message)
    candle = json_message[CANDLE_KEY_BINANCE]

    # Checks if this candle is the closed
    if checkAndPrintCandleClosed(candle):
      # Bynalitics test
      rsi = self.binalytics.threat_binance_message_kline(message)
      if rsi:
        print("BYNALITICS RSI FOUND:", rsi)
        # websocket old variables
        close_price = self.binalytics.last_close_price
        self.last_close_price = close_price
        self.closes.append(close_price)

        # Operates based in market position
        if rsi < RSI_OVERSOLD:
          print("Market Oversold - Trying to push a buy order")
          if self.in_position:
            print("It's is oversold, but already in position and nothing to do")
          else:
              if(self.binSim.order("BUY",ORDER_AMOUT,self.last_close_price)):
                print("BUY ORDER MADE")
                self.in_position = True
                self.binSim.printWalletBalance()              
        elif rsi > RSI_OVERBOUGHT:
          if not self.in_position:
            print("Market is overbought but bot isn't in position")
            print("Waiting for a buy call")
          else:
            print("Market Overbought - Trying to push a sell order")
            if(self.binSim.order("SELL",ORDER_AMOUT,self.last_close_price)):
              print("SELL ORDER MADE")
              self.in_position = False
              self.binSim.printWalletBalance()


  def print_time(self):
    """Prints current time"""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    
  def update(self):
    """This function is called to run the TradeBinBot robot"""
    print("UPDATE STARTED")
    self.print_time()
    self.ws.run_forever()