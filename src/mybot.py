import json,numpy,pprint

from .binbinance.binWebSocket import BinWebSocket
from .binbinance.app_params import *

from binance.enums import *
from binance.client import Client
 

if __name__ == "__main__":
  ws = BinWebSocket(SOCKET)

  print("Starting operation with the following balances:")
  ws.binSim.printWalletBalance()
  
  ### Running Operation
  ws.update() 

  # Print orders when websocket stops
  ws.binSim.printOrders()

  print("FINAL WALLET BALANCE")
  # Print wallet balance when it closes
  ws.binSim.printWalletBalance()

else:
   print("ROBOT NOT RUN")

