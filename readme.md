# Description
## Telegram BOT with the following commands:
- /start - start BOT
- /stop - stop BOT
- /anekdot - get short joke through the parsing site www.anekdot.ru
- /timer - enable/disable the timer. If timer is enabled,the BOT uses the /anekdot command once every 4 hours.

_All informational messages (useless for chat) are deleted after 3 seconds. To do this, the BOT must have the "Admin" status._

## Stack
- python, aiogram
- PyCharm
- DataBase as JSON file in data.json

## Venv
- See requirements.txt

## Project start
- Fill input.env with 2 parameters:
    - BOT_TOKEN
    - ADMIN_ID
- Upload files to the server and run main.py
- ✨Magic ✨