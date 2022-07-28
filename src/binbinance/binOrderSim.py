RSI_PERIOD = 14
RSI_OVERBOUGHT = 0
RSI_OVERSOLD = 10
in_position = False

ORDER_AMOUT = 0.01 

class BinOrderSim:
  """Class used to simulate one internal wallet """
  def __init__(self,wallet_coin, wallet_usdt):
    self.current_coin_balance = wallet_coin
    self.current_usdt_balance = wallet_usdt
    self.orders = []
    self.order_number = 00
    self.in_position = False

  def order(self,type,quantity,price): 
    """Creates one order 

    Args:
        type (string): _description_
        quantity (double): _description_
        price (double): _description_

    Returns:
        bool: Returns True case the order was succesful
    """
    if self.__checkOrder(type,quantity,price):
      #print("Creating order of type {} with quantity {} and price {}".format(type,quantity,price))
      if type == "BUY":
        self.__buy(quantity,price)                                                                    
      if type == "SELL":
        self.__sell(quantity,price)
      order = Order(self.order_number,self.current_usdt_balance,self.current_coin_balance,type,quantity,price,"SUCCESSFUL")
      order.printOrder()
      self.order_number= self.order_number+1
      self.orders.append(order)
      return True        
    else:
      order = Order(self.order_number,self.current_usdt_balance,self.current_coin_balance,type,quantity,price,"FAILED")
      order.printOrder()
      #print("ORDER FAILED")
      self.order_number = self.order_number + 1  
      self.orders.append(order)
      return False      

  def printWalletBalance(self):
    """Prints Current Wallet Balance on screen
    """
    print("COIN BALANCE OF : {}",self.current_coin_balance)
    print("USDT BALANCE OF : {}",self.current_usdt_balance)

  def printOrders(self):
    """Print all of the registered orders
    """
    print("PRINTING ORDERS REGISTER")
    for i in self.orders:
      i.printOrder()

  def simBuyOrder(self):
    """Simulate Buy order
    """
    if self.in_position:
          print("It's is oversold, bot already in position and nothing to do")
    else:
      if(self.order("BUY",ORDER_AMOUT,self.last_close_price)):
        print("BUY ORDER MADE")
        self.in_position = True
        self.printWalletBalance()

  def simSellOrder(self):
    """Simulate Sell Order
    """
    if self.in_position:
          print("It's is oversold, bot already in position and nothing to do")
    else:
      if(self.order("SELL",ORDER_AMOUT,self.last_close_price)):
        print("BUY ORDER MADE")
        self.in_position = False
        self.printWalletBalance()

  def __sell(self,quantity,price):
    """Internal Sell Calculation Function
    """
    cost = quantity*price
    self.current_coin_balance = self.current_coin_balance - quantity
    self.current_usdt_balance = self.current_usdt_balance + cost
      

  def __buy(self,quantity,price):
    """Internal Buy Calculation Function"""
    cost = quantity*price
    self.current_coin_balance = self.current_coin_balance + quantity
    self.current_usdt_balance = self.current_usdt_balance - cost
  
  def __checkOrder(self,type,quantity,price):
    """Internal function for checking if the order is possible

    Args:
        type (string): Order type - "BUY" or "SELL"
        quantity (double): Order quantity
        price (double): Order Price

    Returns:
        bool: _description_
    """
    cost = quantity*price
    if type == "BUY":
      if self.current_usdt_balance - cost < 0:
        #print("INSUFICIENT USDT BALANCE")
        return False 
      else:
        return True 
    if type == "SELL":
      if self.current_coin_balance - quantity < 0:
        #print("INSUFICIENT COIN BALANCE")
        return False
      else:
        return True 
    else:
      return True


class Order():
  """Simple class used for orders
  """
  def __init__(self,order_number,wallet_balance,coin_balance,type,quantity,price,status):
    self.order_number = order_number;
    self.wallet_balance = wallet_balance;
    self.coin_balance = coin_balance
    self.type = type;
    self.quantity = quantity;
    self.price = price;
    self.status = status

  def printOrder(self):
    print("|ORDER NUMBER {} | STATUS {}  | type {} | quantity {} | price {} | w. USDT {} USDT| w. COIN  {}| ".
            format(self.order_number,self.status,self.type,self.quantity,self.price,self.wallet_balance,round(self.coin_balance,4)))

