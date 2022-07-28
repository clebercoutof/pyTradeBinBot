from binance.enums import *
from binance.exceptions import *

class OrderManager:
  """Order Manager Class used to operate with binance"""
  def __init__(self,client):
    self.client = client

  def order(self,symbol,side,type,quantity):
    """Creates a simple Binance Order

    Args:
        symbol (_binance.enums_): Symbol to be traded
        side (_binance.enums_): Side order type
        type (_binance.enums_): Trade type
        quantity (_double_): Order quantity
    """
    try:
      order = self.client.create_order(symbol=symbol
                                      ,side= side
                                      ,type = type
                                      #,timeInForce= TIME_IN_FORCE_GTC
                                      ,quantity=quantity 
                                      #,price='0,01'
                          )
    except BinanceAPIException as e:
      print ("Exception found! Exception status code: " + str(e.status_code))
      print (e.message)

# BUYS BNB WITH BTC
def buyMarketOrderBNBBTC(client,amount):
  """Create one market order for BNBBBTC Type

  Args:
      client (Binance API Client reference): Client used to communicate with binance
      amount (double): Amount to be traded
  """
  try:
    order = client.create_order(symbol='BNBBTC'
                               ,side= SIDE_BUY
                               ,type = ORDER_TYPE_MARKET
                               #,timeInForce= TIME_IN_FORCE_GTC
                               ,quantity=amount 
                               #,price='0,01'
                        )
  except BinanceAPIException as e:
    print ("Exception found! Exception status code: " + str(e.status_code))
    print (e.message)