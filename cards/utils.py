import random


def _generate_deck_index(no_of_possible_cards: int):
    """
    Generates a list of indexes to generate a 30 cards deck that follows the following rules
    1) There can only be a maximum of two of the same cards.


    @param no_of_possible_cards:int : number of possible cards
    @return: index list to generate the deck
    """

    index_list = [num % no_of_possible_cards for num in range(no_of_possible_cards * 2)]
    random.shuffle(index_list)
    new_index_list = index_list[:30]
    new_index_list.sort()
    return new_index_list


def generate_deck(card_list: list):
    """
    Generate a valid 30 cards deck from a list of all possible cards

    @param card_list: list of possible cards
    @return: truncated list of cards
    """

    card_index = _generate_deck_index(len(card_list))
    new_card_list = [card_list[index] for index in card_index]

    return new_card_list
