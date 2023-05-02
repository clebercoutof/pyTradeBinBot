from binance.client import Client
import src.binbinance.logManager as binbinance

if __name__ == "__main__":
  # Client configuration
  client = Client(binbinance.user_cfg.api_key, binbinance.user_cfg.api_secret)
  print("CLIENT LOGGED IN")

  accountInfo = client.get_account()

  # Basic function testing
  binbinance.getAccountBalances(client)
  binbinance.getExchangeInfo(client)
  binbinance.getSymbolInfo(client,'BNBBTC')
  binbinance.buyMarketOrderBNBBTC(client,0.1)

else:
   print("API TEST BROKE")