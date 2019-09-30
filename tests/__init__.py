from cards.utils import _generate_deck_index, generate_deck


class TestUtils:
    def test_generate_deck_index(self):
        deck_index = _generate_deck_index(20)
        assert len(deck_index) == 30
        assert isinstance(deck_index, list)
        assert deck_index[0] <= deck_index[1] <= deck_index[2]

    def test_generate_deck(self):
        mock_card_list = list(range(100))
        deck_list = generate_deck(mock_card_list)
        assert len(deck_list) == 30
        assert len(deck_list) <= len(mock_card_list)
        assert isinstance(deck_list, list)
        assert set(deck_list).issubset(set(mock_card_list))
