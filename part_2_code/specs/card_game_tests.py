import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):


    def test_check_for_ace(self):
        card = Card("diamonds", 2)
        card_game = CardGame()
        result = card_game.check_for_ace(card)
        self.assertEqual(False, result)


    def test_highest_card(self):
        card1 = Card("clubs", 9)
        card2 = Card("spades", 6)
        card_game = CardGame()
        result = card_game.highest_card(card1, card2)
        self.assertEqual(card1, result)

    def test_cards_total(self):
        card1 = Card("clubs", 9)
        card2 = Card("spades", 6)
        card3 = Card("clubs", 10)
        card4 = Card("hearts", 3)
        cards = [card1, card2, card3, card4]
        card_game = CardGame()
        result = card_game.cards_total(cards)
        self.assertEqual( "You have a total of 28", result)