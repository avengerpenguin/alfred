from errbot import BotPlugin, botcmd

class Trello(BotPlugin):

    @botcmd
    def hello(self, msg, args):
        return "Hello, world!"
