from SmartApi import SmartConnect
import pandas as pd
from config import *

obj = SmartConnect(api_key=ANGEL_API_KEY)

def get_index_data(token, exchange="NSE"):

    try:
        session = obj.generateSession(
            ANGEL_CLIENT_ID,
            ANGEL_PASSWORD,
            ANGEL_TOTP
        )

        params = {
            "exchange": exchange,
            "symboltoken": token,
            "interval": "FIVE_MINUTE",
            "fromdate": "2024-01-01 09:15",
            "todate": "2024-01-01 15:30"
        }

        data = obj.getCandleData(params)

        df = pd.DataFrame(data["data"], columns=[
            "time","open","high","low","close","volume"
        ])

        return df

    except Exception as e:
        print(e)
        return None