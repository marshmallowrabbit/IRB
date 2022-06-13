import ccxt

ftx = ccxt.ftx({
    "apiKey": 'YniG9SrlPZ63G47h9sN3hjH-Zjq6hctrkgbdnNF_',
    "secret": 'fsdQqUX7svBRpnY_cKZt9LeikDuz89NCLVN7EB7r',
    "headers": {
        "FTX-SUBACCOUNT": "TestAccount"
    }
})

ftx.load_markets()

symbol = 'ETH-PERP'
type = 'limit'
side = 'buy'
amount = 0.004
price = 1200
params = {
    'stopPrice': 1150,
    # 'ordType': 'StopLimit',
    'takeProfit':1300
}
order = ftx.create_order(symbol, type, side, amount, price, params)


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

