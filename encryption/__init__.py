from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'encryption'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    payment_per_correct = models.CurrencyField()
    word = models.StringField()
    lookup_table = models.StringField()



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    response_1 = models.IntegerField()
    response_2 = models.IntegerField()
    response_3 = models.IntegerField()
    response_4 = models.IntegerField()
    response_5 = models.IntegerField()
    is_correct = models.BooleanField()


# PAGES
class Intro(Page):
    def is_displayed(player):
        return player.round_number == 1

class Decision(Page):
    form_model = "player"
    form_fields = ["response_1",
                   "response_2"]
                   #'response_3',
                   #'response_4',
                   #'response_5']


class Results(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS



page_sequence = [Intro,
                 Decision,
                 Results]
