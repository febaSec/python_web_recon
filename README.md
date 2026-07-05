# Web Recon 🔎🌐

Web Recon is a Python reconnaissance tool that automates subdomain discovery, availability scanning, and change tracking. It integrates Subfinder for reconnaissance, stores historical scan results in SQLite, and sends Telegram notifications whenever new or changed subdomains are detected.

## 🌟 Why this project?

### Automated Reconnaissance

Discover subdomains automatically and monitor them over time without repeating manual reconnaissance.

### Change Detection

The application stores previous scan results in a SQLite database and reports only newly discovered subdomains or status changes.

### Modular Workflow

Reconnaissance, scanning, database operations, logging, and notifications are separated into dedicated modules for maintainability.

---

## 🚀 Quick Start

### Clone the repository

```bash
git clone https://github.com/febaSec/web-recon.git
cd web-recon
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Telegram

Create your environment file:

```bash
cp .env.example .env
nano .env
```

Add:

```text
TG_TOKEN=your_bot_token
TG_CHAT_ID=your_chat_id
```

### Install Subfinder

This project uses **Subfinder** for passive subdomain enumeration.

Verify installation:

```bash
subfinder --version
```

### Run the scanner

```bash
python main.py -d example.com
```

---

## 🔍 Features

- Passive subdomain discovery
- Multi-threaded HTTP availability scanning
- SQLite result storage
- Detection of newly discovered subdomains
- Detection of status changes
- Telegram notifications
- Structured logging
- Rich terminal interface
- Command-line interface

---

## ⚙️ Workflow

```text
Target Domain
      │
      ▼
 Subfinder
      │
      ▼
 Subdomain List
      │
      ▼
 HTTP Scanner
      │
      ▼
 SQLite Database
      │
      ├── Existing → Compare Status
      │
      └── New → Save
                │
                ▼
      Telegram Notification
```

---

## ⚙️ Command Line Options

| Argument | Description |
|----------|-------------|
| `-d, --domain` | Target domain |
| `-t, --threads` | Concurrent scanning threads |
| `-o, --output` | Output file |
| `-v` | Enable verbose logging |

---

## 🛠️ Stack

- Python 3.12
- Subfinder
- Requests
- SQLite3
- Rich
- Python Dotenv
- Telegram Bot API
- ThreadPoolExecutor

---

## 📁 Project Structure

```text
Web-Recon/
├── main.py
├── recon.db
├── recon.log
├── requirements.txt
├── src/
│   ├── discovery.py
│   ├── scanner.py
│   ├── database.py
│   ├── notifier.py
│   ├── utils.py
│   └── __init__.py
└── .env
```

---

## 📊 Example Output

```text
Scanning target: example.com

Discovered: 47 subdomains

Checking HTTP availability...

🆕 NEW:
api.example.com (200)

🆕 NEW:
cdn.example.com (200)

🔄 CHANGE:
old.example.com (0 → 200)
```

Telegram notifications are sent only when new discoveries or status changes are detected.

---

## 📋 Requirements

- Python 3.12+
- Subfinder
- Telegram Bot
- Internet connection

---

## 📄 License

This project is licensed under the MIT License.

See `LICENSE` for more information.
