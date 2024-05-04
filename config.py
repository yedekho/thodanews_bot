#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6846887838:AAG2hH4oXFR4kvdOAyI-M6okCHKdqBBK1RM")

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
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://dotequity:Achiadi123@cluster0.yhav2ul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝗛𝗶𝗶 {first}\n𝗚𝗲𝘁 𝗥𝗲𝗮𝗱𝘆 💪🏻🍌🤤 \n\n𝗣𝗿𝗲𝘀𝘀 𝗦𝗧𝗔𝗥𝗧 𝗮𝗻𝗱 𝗴𝗲𝘁 𝘆𝗼𝘂𝗿 𝗩𝗶𝗱𝗲𝗼 👀\n\n𝗪𝗵𝗮𝘁 𝘁𝗼 𝘄𝗮𝘁𝗰𝗵 🤔😏👉🏻 @linkyaar \n\nQueries/Promotion - @linkyaarbot")
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
USER_REPLY_TEXT = "❌ Do not send any message here\ni cant reply here... 👄 \n\nGet your videos here  👉🏻@linkyaar \n\n Queries/Promotion - @linkyaarbot"

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
