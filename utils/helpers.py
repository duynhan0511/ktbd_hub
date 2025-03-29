# utils/helpers.py

from datetime import datetime

def logger(message: str):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")
    # Nếu muốn ghi ra file log:
    with open("data/logs/crawler.log", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")
