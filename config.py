import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29671179"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c1869ca3064331879fab981eba0342e9")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://hsjsjsjamaksn:LBvy8IZYruLnfPTy@cluster0.eomth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
