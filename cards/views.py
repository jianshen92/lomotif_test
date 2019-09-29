from django.db.models import Q
from django.http import JsonResponse

from cards.models import Cards
from cards.utils import generate_deck


def create_deck(request, player_class: str):
    """

    @param request: HttpRequest object
    @param player_class:str : 1 of the 9 Hearthstone player class

    @return: JsonResponse that contains deck list with 30 cards
    """
    collectible = request.GET.get("collectible", False)
    cards = Cards.objects.filter(
        Q(player_class=player_class) | Q(player_class="Neutral"),
        Q(collectible=collectible),
    ).values("dbf_id", "name", "player_class")

    deck_list = generate_deck(list(cards))

    return JsonResponse(deck_list, safe=False)
