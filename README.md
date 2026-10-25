# 🤖 Telegram Toolbox Bot

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.x-blueviolet?logo=telegram)
![License](https://img.shields.io/badge/license-MIT-green)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white)
![Poetry](https://img.shields.io/badge/Poetry-dependency--manager-yellow?logo=python)

A multifunctional open-source Telegram bot built with Python and [aiogram](https://github.com/aiogram/aiogram). All tools are accessible via inline buttons and fully customizable through FSM-based dialogs.

---

## 🚀 Deploy in one click

<a href="https://render.com/deploy?repo=https://github.com/Aullum/Telegram-Toolbox-Bot">
  <img src="https://img.shields.io/badge/Render-000000?logo=render&logoColor=white&style=for-the-badge" alt="Render" style="height: 35px;"/>
</a>

---

## 🧰 Features

| Tool                 | Description                                      |
| -------------------- | ------------------------------------------------ |
| 🛡 Password Generator | Generate secure passwords with custom settings   |
| 📂 JSON to CSV       | Convert a JSON file (list of objects) to CSV     |
| 🔤 Base64 Tools      | Encode/decode text and files in Base64           |
| 📄 Lorem Ipsum       | Generate 1–15 paragraphs of dummy text           |
| 🧑 Fake Profile      | Generate fake identity profiles by gender/locale |

---

## 🧱 Tech Stack

- **Python 3.12**
- **aiogram 3.x** (async FSM-based bot framework)
- **Poetry** for dependency & project management
- **Docker / docker-compose**
- Modular structure: `handlers / services / keyboards / states`

---

## 🚀 Getting Started

### 🐳 Local with Docker Compose

```bash
git clone https://github.com/YOUR_USERNAME/telegram-toolbox-bot.git
cd telegram-toolbox-bot
cp .env.example .env  # set your BOT_TOKEN

docker-compose up --build -d
```

### 🧪 Manual (Poetry)

```bash
git clone https://github.com/YOUR_USERNAME/telegram-toolbox-bot.git
cd telegram-toolbox-bot
cp .env.example .env  # set your BOT_TOKEN

poetry install
poetry run python main.py
```

---

## 📂 .env.example

```dotenv
BOT_TOKEN=your_telegram_bot_token_here
```

---

## 🖼 Sample UI (via /start)

```
🔧 Choose a tool:

[🛡 Password Generator]
[📂 JSON to CSV]    [🔤 Base64 Tools]
[📄 Lorem Ipsum]    [🧑 Fake Profile]
```

Each tool provides inline UI with options and validation.

---

## 🛠 Project Structure

```
telegram-toolbox-bot/
├── bot/
│   ├── handlers/         # FSM logic per tool
│   ├── services/         # Tool implementations (pure Python)
│   ├── keyboards/        # Inline UI buttons
│   └── states.py         # FSM states
├── main.py               # Entry point
├── pyproject.toml        # Poetry config
├── poetry.lock           # Locked dependencies
├── .env.example
├── .dockerignore         # Docker context exclusions
├── docker-compose.yml
├── Dockerfile
├── render.yaml           # Render deploy config
├── LICENSE               # MIT license
└── README.md
```

---

## 📜 License

MIT — use freely, modify professionally.
