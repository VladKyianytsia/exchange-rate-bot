# Exchange Rate Bot

## Description
- Current UAH/USD exchange rate is fetched every hour from Google Finance and stored in local DB.
- You can get the .xlsx file with all data from Telegram bot

### Technologies used

- Python
- Requests and Beautifulsoup
- SQLAlchemy
- Aiogram
- Celery

### How to use
#### Docker must be installed

1. Fork the repo (GitHub repository)
2. Clone the forked repo
    ```
    git clone the-link-from-your-forked-repo
    ```
3. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
    ```bash
    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt
    ```
4. Create .env file with BOT_TOKEN variable(you can get it from BotFather)
5. Create DB
   ```bash
   python -m db.models
   ```
6. Run bot in terminal
   ```bash
   python -m bot.bot
   ```
7. Run Redis in Docker
   ```bash
   docker run -d -p 6379:6379 redis
   ```
8. Run Celery worker in terminal
   ```bash
   celery -A parser.parser worker --loglevel=info -P solo
   ```
9. Run Celery periodic task
   ```bash
   celery -A parser.parser beat --loglevel=info
   ```
10. Finally, after some time send /get_exchange_rate to your Telegram bot to receive .xlsx file with exchange rates data
