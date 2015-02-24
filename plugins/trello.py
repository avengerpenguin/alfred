import os
from errbot import BotPlugin, botcmd
from trolly.client import Client
from trolly.board import Board
import itertools


class Trello(BotPlugin):

    def __init__(self):
        #self.conn = TrelloConnection('3dd167f33e6de7d4f13fcd138346210c', 'ba57d7a637f46d664b8e30a0d8f50642c55c117dadf23cf7c699c51be5e36cbd')
        self.client = Client(api_key=os.getenv('TRELLO_APP_KEY'), user_auth_token=os.getenv('TRELLO_OAUTH_TOKEN'))
        self.board = Board(self.client, os.getenv('TRELLO_BOARD'))

    def kanban_walker(self):
        flow = reversed(self.board.get_lists())
        for card_list in flow:
            for card in card_list.get_cards():
                yield card

    @botcmd
    def top(self):
        cards = itertools.islice(self.kanban_walker(), 5)
        return '\n'.join([card.get_card_information()['name'] for card in cards])


    @botcmd
    def hello(self, msg, args):
        return "Hello, world!"
