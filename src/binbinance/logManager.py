import json,pprint
from datetime import datetime
from .app_params import *

# Print Exchange Info on Screem
def getExchangeInfo(client):
    """Function used to print exchange info in screen

    Args:
        client (Binance API Client reference): Client used to communicate with binance
    """
    exchange_info = client.get_exchange_info()
    for key,value in exchange_info.items():
        print(key)
        # print(key, " : ", value)

# Print Symbol Info on Screem
def getSymbolInfo(client,symbol):
    """Function used to print the input symbol info in screen


    Args:
        client (Binance API Client reference): Client used to communicate with binance
        symbol (_string_): Symbol - ex: ('BNBBTC')
    """
    info = client.get_symbol_info('BNBBTC')
    for key,value in info.items():
        # print(key)
        print(key, " : ", value)

#Print Account Wallet Ballances
def getAccountBalances(client):
    """Gets the Account Balances that aren't zero and display them on screen

    Args:
        client (Binance API Client reference): Client used to communicate with binance
    """
    accountInfo = client.get_account()
    balances = accountInfo["balances"]
    print("Showing account avaiable balances")
    for i in balances: 
        value = float(i['free'])
        value_string = i['free']
        moeda = i['asset']
        if value > 0.0:
            print("COIN:" + moeda + "/ AMOUNT:" + value_string)

# Print Received KLine Message
def printKlineMesage(message):
    """Prints the received Kline message

    Args:
        message (_string_): Message received from binance websocket
    """
    json_message = json.loads(message)
    pprint.pprint(json_message)

# Print Received KLine Message with full description
def printKlineLongMessage(message):
    """Prints the received Kline message with the drescription for all items

    Args:
        message (_string_): Message received from binance websocket
    """
    json_message = json.loads(message)
    updateMessageTimestamp(json_message)
    long_message = createLongMessageKline(json_message)
    pprint.pprint(long_message)
    
# Creats Kline message with full description
def createLongMessageKline(message):
    """Generates the KLine message with full description for all items

    Args:
        message (_string_): Message received from binance websocket

    Returns:
        _string_: Message with full description for the itens
    """
    long_message = message
    for old_key in message[CANDLE_KEY_BINANCE]:
        if old_key in KLINE_DESCRIPTION_DICT.keys():
            new_key = KLINE_DESCRIPTION_DICT[old_key];
            long_message[CANDLE_KEY_BINANCE][new_key] = long_message[CANDLE_KEY_BINANCE][old_key]
            del long_message[CANDLE_KEY_BINANCE][old_key]
    return long_message

# Updates the message timestamp do DATETIME format
def updateMessageTimestamp(message):
    """Updates the message timestamp to timedate

    Args:
        message (_json_message_): JSON message 
    """
    for key in message.keys():
        if key == TIMESTAMP_DATA_KEY_BINANCE:
            message["Date Time"] = str(datetime.fromtimestamp(message[key]/TIMESTAMP_TO_MS))  
            del message[TIMESTAMP_DATA_KEY_BINANCE]

# Converts received datime from dms
def updateTimestampToDatetimeMs(value):
    return str(datetime.fromtimestamp(value/TIMESTAMP_TO_MS))  

# Checks if message has closed candle
def checkCandleClosed(candle_message):
    """Checks if the input message represents the close candle

    Args:
        candle_message (_json_message_): _description_

    Returns:
        _bool_: Returns the true if the message repesents a close candle
    """
    is_candle_closed = candle_message[CANDLE_CLOSED_KEY_BINANCE]
    if is_candle_closed:
        return True

# Checks if message has closed candle and prints the closing price
def checkAndPrintCandleClosed(candle_message):
    """Checks if the input message represents the close candle and prints current closing price

    Args:
        candle_message (_json_message_): _description_

    Returns:
        _bool_: Returns the true if the message repesents a close candle
    """
    is_candle_closed = candle_message[CANDLE_CLOSED_KEY_BINANCE]
    close_price = candle_message[CLOSE_PRICE_KEY_BINANCE]

    if is_candle_closed:
        print("Candle closed on value: " + str(close_price) + " on time: " + updateTimestampToDatetimeMs(candle_message[CANDLE_TIMESTAMP_KEY_BINANCE]) )
        return True