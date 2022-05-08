def goLong(df,symbol,amount):
    type = 'limit'  # or 'market', other types aren't unified yet
    side = 'sell'
    price = 54.321  # your price
    # overrides
    params = {
        'stopPrice': 123.45,  # your stop price
        'type': 'stopLimit',
    }
    order = exchange.create_order(symbol, type, side, amount, price, params)
