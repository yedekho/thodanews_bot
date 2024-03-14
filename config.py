#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7004110350:AAHPgVXuhbOoTvqWbFY4ls7cJk5tbB-t8_w")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29996160"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "55305b23a72c1e001a0fb21b7bfe0785")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002014585511"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5089010547"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://dotequity:Achiadi123@cluster0.hst9mig.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Heyaa 👀 {first}\n\n𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖶𝗈𝗋𝗅𝖽 𝗈𝖿 \n@wownewsss 👽☠️ \n\n𝖦𝖾𝗍 𝗋𝖾𝖺𝖽𝗒 𝗍𝗈 𝖾𝗑𝗉𝖾𝗋𝗂𝖾𝗇𝖼𝖾 𝗍𝗁𝖾 \n𝖡𝗋𝗎𝗍𝖺𝗅𝗂𝗍𝗒 🔪😳 𝖺𝗇𝖽 𝖳𝗁𝗋𝗂𝗅𝗅𝖾𝗋 🤯 ... \n\n𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆 - @𝗐𝗈𝗐𝗇𝖾𝗐𝗌𝗌 ❤️ \n𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 - @wownewsss 💙 \n𝖳𝗁𝗂𝗌 𝖻𝗈𝗍 𝗐𝗂𝗅𝗅 𝗀𝗂𝗏𝖾 𝗒𝗈𝗎𝗋 𝗏𝗂𝖽𝖾𝗈𝗌 🎦 \nयह बॉट आपके वीडियो देगा 🎦 \nسيعطي هذا الروبوت مقاطع الفيديو الخاصة")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
