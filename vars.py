

from os import environ

API_ID = int(environ.get("API_ID", "23878955"))
API_HASH = environ.get("API_HASH", "07637a6c4c4566dc3923fa29d6c84b67")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "free_for_All_User")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/free_for_All_User")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "5445688589").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "5445688589"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")







