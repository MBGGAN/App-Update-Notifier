
# 📱 App Update Notifier

This Python script checks for version updates of selected Android apps on the **Google Play Store**, and sends alerts to **Telegram** and **Discord** when a new version is detected.

It runs automatically every hour using **GitHub Actions** – no server or hosting required.

---

## 🔔 Features

- 🔄 Monitors any number of Android apps by package name
- 📤 Sends update notifications to:
  - Telegram bot
  - Discord webhook
- 🕒 Auto-runs hourly via GitHub Actions
- 🧠 Remembers last notified versions (stored in a JSON file)

---

## 🛠 Requirements

To use this project, you’ll need:

- A [Telegram bot token](https://t.me/BotFather)
- A Telegram **chat ID**
- A Discord webhook URL
- A GitHub account

---

## 🚀 Setup Instructions

### 1. 💾 Fork or clone the repository

```bash
git clone https://github.com/your-username/app-update-notifier.git
cd app-update-notifier
```

---

### 2. 🧠 Add your apps to monitor

In `main.py`, edit the `apps_to_monitor` dictionary:

```python
apps_to_monitor = {
    "Minecraft PE": "com.mojang.minecraftpe",
    "ToolBox": "io.mrarm.mctoolbox",
    "Your App Name": "com.example.yourapp"
}
```

You can find app package names from their Google Play URLs, like:

```
https://play.google.com/store/apps/details?id=com.example.app
```

---

### 3. 🔐 Add GitHub Secrets

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**, and add the following:

| Secret Name             | Example Value                        |
|------------------------|--------------------------------------|
| `TELEGRAM_BOT_TOKEN`   | `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` |
| `TELEGRAM_CHAT_ID`     | `123456789`                          |
| `DISCORD_WEBHOOK_URL`  | `https://discord.com/api/webhooks/...` |

> You can get your Telegram chat ID by messaging your bot and visiting:
> `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

---

### 4. ⚙️ GitHub Actions Workflow

No changes needed! The included workflow (`.github/workflows/run.yml`) will:

- Install dependencies
- Run `main.py` every hour
- Use your GitHub secrets

---

## 🧪 Local Testing (Optional)

To run the script manually on your computer:

```bash
pip install -r requirements.txt
python main.py
```

---

## 📂 Project Structure

```
.
├── main.py                 # Main script
├── requirements.txt        # Python dependencies
├── app_versions.json       # Stores last known versions
└── .github
    └── workflows
        └── run.yml         # GitHub Actions workflow
```

---

## ✅ Example Output

### Telegram / Discord Message

```
New update available for Minecraft PE!
Latest Version: 1.20.50.21
Previous Version: 1.20.41.01
Check it out: https://play.google.com/store/apps/details?id=com.mojang.minecraftpe
```

---

## 📄 License

This project is licensed under the MIT License — feel free to use or modify it.

---

## 👨‍💻 Credits

Made with 💻 and ☕ by [Metro]
