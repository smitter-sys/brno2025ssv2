from otree.api import *
from pip._internal import models

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    ENDOWMENT = 10
    COST_PER_TICKET = 0.5
    PRIZE = 8

class Subsession(BaseSubsession):
    csf = models.StringField()
    is_paid = models.BooleanField

class Group(BaseGroup):
    cost_per_ticket = models.CurrencyField()
    Prize = models.CurrencyField()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    tickets_purchased = models.IntegerField()
    prize_won = models.FloatField()
    earnings = models.CurrencyField()


# PAGES
class StartRound(WaitPage):
    pass

class Intro(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Decision(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


class EndBlock(Page):
    pass


page_sequence = [
    StartRound,
    Intro,
    Decision,
    ResultsWaitPage,
    Results,
    EndBlock,
]
