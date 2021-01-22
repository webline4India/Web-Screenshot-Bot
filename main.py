from pyrogram import Client
from creds import my

plugins = dict(root="plugins")
app = Client(
    "Webshot Bot",
    bot_token=my.1573785521:AAGOyjl0Mfok6z-HNmd25X7lS3ZC82vlI1g,
    api_id=my.2421844,
    api_hash=my.779fe41a408add3441fd599d8e77c984,
    plugins=plugins,
)

app.run()
