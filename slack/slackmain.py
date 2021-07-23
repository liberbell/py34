import requests

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to

bot = Bot()
# bot.run()
@respond_to('practice')

def respond(message):
    message.send("This is a practie right?")

@listen_to("game")

def linsten(message):
    message.send("This is not drill.")

bot.run()