
# 📱 App Update Notifier

This Python script checks for version updates of selected Android apps on the **Google Play Store**, and sends alerts to **Telegram** and **Discord** when a new version is detected.

It runs automatically every 10 minutes using **GitHub Actions** – no server or hosting required.

---

## 🔔 Features

- 🔄 Monitors any number of Android apps by package name
- 📤 Sends update notifications to:
  - Telegram bot
  - Discord webhook
- 🕒 Auto-runs every 10 minutes via GitHub Actions
- 🧠 Remembers last notified versions (stored in a JSON file)
- 🔐 SSH-based secure file updates

---

## 🛠 Requirements

To use this project, you’ll need:

- A [Telegram bot token](https://t.me/BotFather)
- A Telegram **chat ID**
- A Discord webhook URL
- A GitHub account
- **SSH key** for secure file updates (if deploying or updating via GitHub Actions)

---

## 🚀 Setup Instructions

### 1. 💾 Fork or clone the repository

```bash
git clone https://github.com/MBGGAN/App-Update-Notifier.git
cd App-Update-Notifier
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
| `SSH_PRIVATE_KEY`      | `YOUR_SSH_PRIVATE_KEY_HERE`          |

> You can get your Telegram chat ID by messaging your bot and visiting:
> `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`

> You can generate your SSH key pair and add the **private key** to this secret for secure file updates.

---

### 4. ⚙️ GitHub Actions Workflow

No changes needed! The included workflow (`.github/workflows/run.yml`) will:

- Install dependencies
- Set up SSH for secure file updates
- Run `main.py` every 10 minutes
- Use your GitHub secrets for Telegram, Discord, and SSH

---

### 5. **Set up SSH for Secure File Updates**

If you are using SSH to securely update your files (e.g., if you're deploying this script to a server or need to pull updates from GitHub), follow these steps:

#### Step 1: **Generate an SSH Key Pair**

On your local machine or server, generate an SSH key pair (if you don't have one already) with:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

This will generate two files:
- **Private key**: usually stored as `~/.ssh/id_rsa`
- **Public key**: stored as `~/.ssh/id_rsa.pub`

#### Step 2: **Add the Public Key to GitHub**

Go to your GitHub account, and navigate to **Settings** → **SSH and GPG Keys** → **New SSH Key**. Copy the content of the public key (`id_rsa.pub`) and paste it there.

#### Step 3: **Add the Private Key to GitHub Secrets**

1. Go to your repository → **Settings** → **Secrets** → **New repository secret**
2. Name the secret `SSH_PRIVATE_KEY` and paste the contents of your private key (`id_rsa`) as the value.

#### Step 4: **Update the GitHub Actions Workflow**

Update the `.github/workflows/run.yml` file to include SSH setup for secure file updates:

```yaml
name: Run App Update Notifier

on:
  schedule:
    - cron: "*/10 * * * *"
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up SSH key
      uses: webfactory/ssh-agent@v0.5.3
      with:
        ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run the script
      run: python main.py
```

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

