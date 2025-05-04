import os
import requests
import json
from telegram import Bot
from google_play_scraper import app

# Load tokens from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

apps_to_monitor = {
    "Minecraft PE": "com.mojang.minecraftpe",
    "Lunar Client": "localhost.lunar",
}

PLAY_STORE_URL = "https://play.google.com/store/apps/details?id={}"
DATA_FILE = "app_versions.json"

def load_last_notified_versions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_last_notified_versions(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_latest_version(app_id):
    try:
        result = app(app_id)
        return result.get("version")
    except Exception as e:
        print(f"Error fetching version for {app_id}: {e}")
    return None

def send_notification(app_name, latest_version, app_id, last_version=None):
    message = f"New update available for {app_name}!\nLatest Version: {latest_version}"
    if last_version:
        message += f"\nPrevious Version: {last_version}"
    message += f"\nCheck it out: {PLAY_STORE_URL.format(app_id)}"

    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        print("Error sending message to Telegram:", e)

    ping = "<@1077815215397294081> "
    discord_data = {"content": ping + message}
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=discord_data)
    except requests.RequestException as e:
        print("Error sending message to Discord:", e)

def check_for_updates():
    last_notified_versions = load_last_notified_versions()
    updated = False

    for app_name, app_id in apps_to_monitor.items():
        latest_version = get_latest_version(app_id)
        last_version = last_notified_versions.get(app_id)
        if latest_version and latest_version != last_version:
            send_notification(app_name, latest_version, app_id, last_version)
            last_notified_versions[app_id] = latest_version
            updated = True

    if updated:
        save_last_notified_versions(last_notified_versions)

if __name__ == "__main__":
    check_for_updates()
