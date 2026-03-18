import schedule
import time
from angel_data import get_index_data
from strategy import generate_signal, get_strike
from telegram import send_telegram
from news import get_news, get_order_news


def send_signal(name, signal, price, rsi):

    ce, pe = get_strike(price)
    strike = ce if signal == "BUY" else pe

    msg = f"""
🚀 HIGH ACCURACY SIGNAL

Index: {name}
Signal: {signal}
Price: {round(price,2)}

🎯 Strike: {strike}

RSI: {round(rsi,2)}

👉 Action:
{"BUY CE" if signal=="BUY" else "BUY PE"}

🛑 SL: 1%
🎯 Target: 2-3%
"""

    send_telegram(msg)


def run_bot():
    try:
        print("📊 Running strategy...")

        nifty = get_index_data("99926000")
        banknifty = get_index_data("99926009")

        for name, data in [("NIFTY", nifty), ("BANKNIFTY", banknifty)]:

            if data is None or len(data) < 30:
                print(f"⚠️ No data for {name}")
                continue

            signal, rsi, price = generate_signal(data)

            print(f"{name} → Signal: {signal}")

            if signal != "HOLD":
                send_signal(name, signal, price, rsi)

    except Exception as e:
        print("❌ Error in run_bot:", e)
        send_telegram(f"❌ BOT ERROR: {e}")


def send_news():
    try:
        print("📰 Sending news...")

        news = get_news()
        orders = get_order_news()

        msg = "📰 MARKET NEWS\n\n"

        for n in news:
            msg += f"• {n}\n"

        msg += "\n🔥 ORDER NEWS\n\n"

        for o in orders:
            msg += f"• {o}\n"

        send_telegram(msg)

    except Exception as e:
        print("❌ Error in news:", e)


# ⏰ Scheduling
schedule.every(5).minutes.do(run_bot)
schedule.every(30).minutes.do(send_news)

print("🚀 BOT STARTED (RAILWAY MODE)")
send_telegram("🚀 BOT STARTED (RAILWAY LIVE)")

# 🔁 Infinite loop (Railway ke liye must)
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print("❌ Loop Error:", e)
        time.sleep(5)