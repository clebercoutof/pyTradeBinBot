from .logManager import checkCandleClosed
import numpy,talib,json
from .binOrderSim import *
from .logManager import *
from .app_params import *

class Binalytics:
  """Bin Analytics Class for data threatment, storage, and index calculation"""
  def __init__(self):
    self.closes = []
    self.last_close_price = 0
    #self.binSim = BinOrderSim()
    self.lastRSI = 0
    
  def threat_binance_message_kline(self,message):
    """Threats the binance message and computes the RSI case it's possible

    Args:
        message (string): Received websocket full message

    Returns:
        double: Returns the RSI index case it's possible to calculate
    """
    json_message = json.loads(message)
    candle = json_message[CANDLE_KEY_BINANCE]

    rsi = 0
    if checkCandleClosed(candle):
      close_price = float(json_message[CANDLE_KEY_BINANCE][CLOSE_PRICE_KEY_BINANCE])
      self.last_close_price = close_price
      self.closes.append(close_price)
      rsi = self.checkAndComputeRSI()
    if rsi:
        return rsi
    else:
      return False

  #Function that computes rsi and returns false case there is no way to compute it
  def checkAndComputeRSI(self):
    """Checks if it's possible to compute RSI and calculates

    Returns:
        double: Returns the RSI index case it's possible to calculate
    """
    if len(self.closes) > RSI_PERIOD:
      np_closes = numpy.array(self.closes)
      rsi = talib.RSI(np_closes,RSI_PERIOD)
      self.lastRSI = rsi[-1]
      #print("Currently RSI: " + str(self.lastRSI) + " Last Closing Price:" + str(self.last_close_price))
      return self.lastRSI
    else:
      return False


  #Function used to test RSI with fake closes array
  def threatClosesFakeArray(self,closes_input):
    """Function used for testing with fake closes array input

    Args:
        closes_input (double array): Array containing the fake closes
    """
    # Cleans internal variable only for guarantee
    self.closes = []
    self.last_close_price = 0
    for close_price in closes_input:
      print("Current close price:", close_price)
      self.closes.append(close_price)
      self.last_close_price = close_price
      aray_len = len(self.closes)

      if aray_len > RSI_PERIOD:
        rsi = self.checkAndComputeRSI()
        self.lastRSI = rsi[-1]
        if rsi:
          print("RSI FOUND:" + str(rsi))

    def __getMessageClosePrice(self,json_message):
      """Internal function for getting candle message close price

      Args:
          json_message (string): Json converted message
      """
      close_price = float(json_message[CANDLE_KEY_BINANCE][CLOSE_PRICE_KEY_BINANCE])
      self.last_close_price = close_price
      self.closes.append(close_price)
