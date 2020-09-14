import random

class Deck:

    # инициализация колоды
    def __init__(self):
        self.__suits = ["\u2660", "\u2665", "\u2663", "\u2666"]
        self.__cards = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = {self.__cards[i]: i for i in range(len(self.__cards))}
        _ls_mix_deck = []
        # self._cards_dict = {__cards[i]: i for i in range(len(__cards))}
        self.all_deck = {}
        for i in range(len(self.__suits)):
            for key, values in self.deck.items():
                key = self.__suits[i] + key
                self.all_deck[key] = values

    # Перемешивание колоды
    def mix_deck(self):
        self._ls_mix_deck = list(self.all_deck)
        random.shuffle(self._ls_mix_deck)

    # Раздача карт
    def hand_cards(self):
        self.player_hand = self._ls_mix_deck[-6:]
        self._computer_hand = self._ls_mix_deck[-12:-6]
        del self._ls_mix_deck[-12:]

    # Жребий кто ходит первым
    def first_turn(self):
        if random.randint(1, 2) == 1:
            print('Ходит Игрок')
            return 'Ходит Игрок'
        else:
            print('Ходит Компьютер')
            return 'Ходит Компьютер'

    # Игрок ходит
    def turn(self):
        print('Ваши карты:\n{}'.format(self.player_hand))
        self.player_card = []
        self.player_hand_len = []
        for i in range(len(self.player_hand)): # выводим для удобства цифры (сколько карт в рукаве) для пользователя
            self.player_hand_len.append(i)
        self.player_choice = int(input('Введите карту, которой желаете пойти: {}'.format(self.player_hand_len)))
        self.player_card.append(self.player_hand[self.player_choice])
        self.player_hand.remove(self.player_hand[self.player_choice])

    # Компьютер отвечает
    def computer_answer(self):
        self.answer_cards = []
        for card in self._computer_hand:
            if (card[0:1] == self.player_card[0][0:1]):
                if self.all_deck[card] > self.all_deck[self.player_card[0]]:
                    self.answer_cards.append(card)

        if len(self.answer_cards) > 0:
            self.computer_move = self.answer_cards[0]
            self._computer_hand.remove(self.computer_move)
            print('Компьютер бьет Вашу карту картой {}.'.format(self.computer_move))
            return 'Ход Компьютера'
        else:
            print('Компьютер берет.')
            self._computer_hand.append(self.player_card)
            return 'Ход Игрока'

if __name__ == '__main__':
    deck_test = Deck()
    deck_test.mix_deck() # Перемешиваем колоды
    deck_test.hand_cards() # Раздаем карты
    turn_start = deck_test.first_turn()
    deck_test.turn()
    deck_test.computer_answer()
    print(deck_test.player_card)
    print(deck_test.answer_cards)
#    print(deck_test.computer_move)