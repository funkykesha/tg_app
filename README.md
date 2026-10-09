# tg_app

Telegram Mini App: сегодняшняя дата + курс валют ЦБ РФ.

```
webapp/index.html   — сама мини-апп (статика, Telegram WebApp SDK)
bot/bot.py          — бот на aiogram: кнопка /start + menu button
.github/workflows/  — автодеплой webapp/ на GitHub Pages
```

## Запуск

1. **Хостинг мини-аппа** (нужен HTTPS): Settings → Pages → Source: *GitHub Actions*.
   После пуша в `main` приложение будет на `https://funkykesha.github.io/tg_app/`.
2. **Бот**:
   ```bash
   cd bot
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env   # вписать BOT_TOKEN
   python bot.py
   ```
3. В Telegram: `/start` → кнопка «💱 Курс валют».

Курсы: https://www.cbr-xml-daily.ru/daily_json.js (бесплатно, без ключа, CORS открыт).
