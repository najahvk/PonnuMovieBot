import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '22369181'))
API_HASH = environ.get('API_HASH', '7dad13f46bdcd58805ce9f9ebb13c8ee')
BOT_TOKEN = environ.get('BOT_TOKEN', '8101559551:AAGW40LT9kFcdQtVhIyy2WbfUATKDjdrCXA')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1769132732 6861922941 7457122085 7033932663').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/ponnuXmol')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002596835060'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1003029942992').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://najahvk6_db_user1:najahvk6_db_user1@cluster0000.ihzvxpi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0000")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://najahvk6_db_user2:najahvk6_db_user2@cluster0000.oy7impi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0000")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'TheNuwSav3Jdj')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002596835060'))
QR_CODE = environ.get('QR_CODE', 'https://')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
OWNER_LINK = environ.get('OWNER_LINK', 'https://telegram.me/ponnuXmol')
MOVI_GRP = environ.get('MOVI_GRP', 'https://t.me/PonnuMovieGroup')
MOVI_CHNL = environ.get('MOVI_CHNL', 'https://t.me/PonnuMovie')
PICZ = (environ.get('PICZ', 'https://i.ibb.co/tT15Txc9/IMG-20250930-WA0064.jpg https://i.ibb.co/mVhRWSF0/IMG-20250930-WA0067.jpg https://i.ibb.co/d4bhZ8MR/IMG-20250930-WA0066.jpg https://i.ibb.co/jPqkPHxj/IMG-20250930-WA0065.jpg')).split()
#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002596835060'))
URL = environ.get('URL', 'https://render.com/botbsbsbbshbs/')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002780984382'))
TUTORIAL = environ.get("TUTORIAL", "https://youtu.be/0c-i2Lol6LU")
TUTORIAL2 = environ.get("TUTORIAL2", "https://youtu.be/GdaUbzxDTKs")
TUTORIAL3 = environ.get("TUTORIAL3", "https://youtu.be/rddlpYLm0G0")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "8c09653e5c38f84d1b76ad3197c5a023e53b494d")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "onepagelink.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "0c8ebd63bfe9f67f9970b8767498ff60316b9b03")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "tnshort.net")
SHORTENER_API3 = environ.get("SHORTENER_API3", "9c5a6c96077a1b499d8f953331221159383eb434")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1003117328540')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002596835060'))


# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '10'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', False)
LINK_MODE = is_enabled('LINK_MODE', False)
PM_SEARCH = is_enabled('PM_SEARCH', True)
