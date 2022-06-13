import ccxt

ftx = ccxt.ftx({
    "apiKey": 'YniG9SrlPZ63G47h9sN3hjH-Zjq6hctrkgbdnNF_',
    "secret": 'fsdQqUX7svBRpnY_cKZt9LeikDuz89NCLVN7EB7r',
    "headers": {
        "FTX-SUBACCOUNT": "TestAccount"
    }
})
    
def Order(trade_type,limit_price,stop_price,target_price):
    ftx.createOrder()
    ftx.createStopLimitOrder()
    ftx.createStopOrder()
    params = {}
    setLeverage (leverage, symbol = undefined, params = {})
