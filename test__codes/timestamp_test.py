from datetime import datetime

if __name__ == "__main__":
  binance_timestamp = 1658188649193
  timestamp_miliseconds = binance_timestamp/1000
  date = datetime.fromtimestamp(timestamp_miliseconds)
  print(date)