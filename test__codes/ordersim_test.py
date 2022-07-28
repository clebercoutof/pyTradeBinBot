import sys
import os
from src.binbinance.binOrderSim import BinOrderSim

if __name__ == "__main__":
  WALLET_COIN = 0
  WALLED_USDT = 50
  binSim = BinOrderSim(WALLET_COIN,WALLED_USDT)
  
  buy_quantity= 0.2
  market_price = 100
  binSim.order("BUY",buy_quantity,market_price)

  sell_quantity = 0.15
  binSim.order("SELL",sell_quantity,market_price)

  sell_quantity = 0.03
  binSim.order("SELL",sell_quantity,market_price)

  sell_quantity = 0.01
  binSim.order("SELL",sell_quantity,market_price)

  sell_quantity = 0.01
  binSim.order("SELL",sell_quantity,market_price)
  binSim.order("SELL",sell_quantity,market_price)
  binSim.order("SELL",sell_quantity,market_price)
  binSim.order("SELL",sell_quantity,market_price)
  binSim.order("SELL",sell_quantity,market_price)
  binSim.order("SELL",sell_quantity,market_price)
  binSim.order("SELL",sell_quantity,market_price)

  buy_quantity= 0.02
  binSim.order("BUY",buy_quantity,market_price)
  binSim.order("BUY",buy_quantity,market_price)
  binSim.order("BUY",buy_quantity,market_price)
  binSim.order("BUY",buy_quantity,market_price)
  binSim.order("BUY",buy_quantity,market_price)
  binSim.order("BUY",buy_quantity,market_price)
  binSim.printOrders()
  # order_= BinOrderSim()