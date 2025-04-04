import os import requests from flask import Flask from apscheduler.schedulers.background import BackgroundScheduler

Ganti dengan TOKEN BOT Telegram-mu

token = "YOUR_TELEGRAM_BOT_TOKEN"

Ganti dengan chat_id / group_id tujuan

chat_id = "YOUR_CHAT_ID"

app = Flask(name) scheduler = BackgroundScheduler()

def send_airdrop_reminder(): message = "\U0001F4B0 Daily Airdrop Reminder! \U0001F4B0\n\nJangan lupa klaim airdrop hari ini! Klik link di bawah ini:\n\n" 
"Klaim Airdrop"

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown",
    "disable_web_page_preview": True
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print("Pesan terkirim!")
else:
    print("Gagal mengirim pesan:", response.text)

Menjadwalkan pengiriman pesan setiap hari jam 07:00

scheduler.add_job(send_airdrop_reminder, 'cron', hour=7, minute=0, timezone='UTC') scheduler.start()

@app.route('/') def index(): return "Airdrop Reminder Bot is running!"

if name == 'main': app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

File requirements.txt

""" flask apscheduler requests gunicorn """

File Procfile

""" web: gunicorn app:app """

