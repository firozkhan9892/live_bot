from indicators import *

def get_strike(price, step=50):

    atm = round(price / step) * step

    ce = f"{atm} CE"
    pe = f"{atm} PE"

    return ce, pe


def generate_signal(data):

    rsi = calculate_rsi(data)
    breakout = breakout_check(data)
    breakdown = support_break(data)
    volume = volume_spike(data)

    price = data["close"].iloc[-1]
    ema = data["close"].ewm(span=20).mean().iloc[-1]

    # sideways filter
    range_ = data["high"].rolling(20).max().iloc[-1] - data["low"].rolling(20).min().iloc[-1]

    if range_ < price * 0.5/100:
        return "HOLD", rsi, price

    if rsi > 55 and breakout and volume and price > ema:
        return "BUY", rsi, price

    if rsi < 45 and breakdown and volume and price < ema:
        return "SELL", rsi, price

    return "HOLD", rsi, price