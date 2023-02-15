from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("26641701")
APP_HASH = os.environ.get("5a0a7208eb91f3623258c4f4bb3abf0a")
BOT_USERNAME = os.environ.get("iqthon9181766bot")
session = os.environ.get("1ApWapzMBu4YcdmfW3nzFvDfrJ8xjCsAZd8gSrhEzsu7bj2K4dSPxXDWqrJhJuGeJxY0sQjpwRDHus-Bv1NhPoaZjYSfwuAVPkWVP3FlsZ82ocAlnT8ZqtsqlEl9N2wSY4BeZH8K6lFbDc2jCz7nyqN3NICzqDLJuRZp3jFW_yWU4OORQwWOWaF3TGfWVrI9HEOBmRo-vEoMVH2VFiIPX1oGbkixxcWeo7pbDWVSYCBIyxLgbKjiH4_0QP11LipierQ7oJlfdQ9cUffgnj8MSEAE8T8aB31Kq_1JtGVZMHIJS56qQvwW5Q3To9Vzv4xxLyAtxraHZIxBSx0qw4yXyYC6cBF_1mOw=")
SESSION = os.environ.get("1ApWapzMBu4YcdmfW3nzFvDfrJ8xjCsAZd8gSrhEzsu7bj2K4dSPxXDWqrJhJuGeJxY0sQjpwRDHus-Bv1NhPoaZjYSfwuAVPkWVP3FlsZ82ocAlnT8ZqtsqlEl9N2wSY4BeZH8K6lFbDc2jCz7nyqN3NICzqDLJuRZp3jFW_yWU4OORQwWOWaF3TGfWVrI9HEOBmRo-vEoMVH2VFiIPX1oGbkixxcWeo7pbDWVSYCBIyxLgbKjiH4_0QP11LipierQ7oJlfdQ9cUffgnj8MSEAE8T8aB31Kq_1JtGVZMHIJS56qQvwW5Q3To9Vzv4xxLyAtxraHZIxBSx0qw4yXyYC6cBF_1mOw=")
token = os.environ.get("5920496145:AAHa6yfqQgdQoO5DGmV4ZxGta5Ihpc7hSn0")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
