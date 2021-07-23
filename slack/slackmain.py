import requests

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to

bot = Bot()
# bot.run()
@respond_to('practice')

def sample(message):
    message.send("This is a practie right?")

bot.run()