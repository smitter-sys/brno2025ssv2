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
    reponse_1 = models.IntegerField()
    reponse_2 = models.IntegerField()


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Intro,
                 Decision,
                 Results]
