import ccxt

ftx = ccxt.ftx({
    "apiKey": 'YniG9SrlPZ63G47h9sN3hjH-Zjq6hctrkgbdnNF_',
    "secret": 'fsdQqUX7svBRpnY_cKZt9LeikDuz89NCLVN7EB7r',
    "headers": {
        "FTX-SUBACCOUNT": "TestAccount"
    }
})

symbol = 'ETH-PERP'
order_type = 'limit'
# type_2 = 'StopLimit'
# type_3 = 'TakeProfitLimit'
order_side = 'buy'
# side_2 = 'sell'
amount = 0.004
price = 1082
stop_price = 1000
takeProfit_price = 1280


def Order(symbol,order_type,order_side,amount,price,stop_limit,target_limit):
    ftx.load_markets()
    ftx.cancel_all_orders(symbol,params={'conditionalOrdersOnly': True})
    ftx.cancel_all_orders(symbol)
    
    order = ftx.create_order(symbol, type = order_type, side = order_side, amount = amount, price = price)
    stoploss = ftx.create_order(symbol, type = 'StopLimit', side = 'sell', amount = amount, price = stop_price, params = {'stopPrice': stop_price,'ordType': 'StopLimit'})
    takeprofit = ftx.create_order(symbol, type = 'TakeProfitLimit', side = 'sell', amount = amount, price = takeProfit_price, params = {'takeProfitPrice': takeProfit_price,'ordType': 'TakeProfitLimit'})

Order(symbol,order_type,order_side,amount,price,stop_price,takeProfit_price)

# THIS CODE RESULTS IN A STOP LOSS AND TAKE PROFIT TRIGGER ORDER HOWEVER, IF STOPLOSS IS TRIGGERED THEN TAKEPROFIT REMAINS AND VICE-VERSA


# ethPrice = 1000
# stopPrice = 5000
# trailingOrder = exchange.create_order(symbol, type = 'StopLimit', side, amount, price, params = {
#     'stopPrice': 1150,
#     'ordType': 'StopLimit',
#     'pegPriceType': 'TrailingStopPeg',
#     'pegOffsetValueEp': 10000, # needs to be scaled
#     'triggerType': 'ByMarkPrice'
#     })



# def Order(trade_type,limit_price,stop_price,target_price):
#     ftx.createOrder()
#     ftx.createStopLimitOrder()
#     ftx.createStopOrder()
#     params = {}
#     setLeverage (leverage, symbol = undefined, params = {})

