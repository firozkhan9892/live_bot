def calculate_rsi(data, period=14):
    delta = data["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100/(1+rs))

    return rsi.iloc[-1]


def breakout_check(data):
    return data["close"].iloc[-1] > data["high"].rolling(20).max().iloc[-2]


def support_break(data):
    return data["close"].iloc[-1] < data["low"].rolling(20).min().iloc[-2]


def volume_spike(data):
    avg_vol = data["volume"].rolling(20).mean().iloc[-2]
    return data["volume"].iloc[-1] > avg_vol * 1.8