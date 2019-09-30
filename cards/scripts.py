"""
This script is meant to be run once to populate database with cards in Rastakhan Rumble Set
"""

import requests
from django.db import transaction

from cards.models import Cards

url = "https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble"
headers = {"X-Mashape-Key": "ZTMJtzbYvXmshPTFEZI4ztIy3I68p1nPwgHjsnIGukKZeJxGcs"}

# Send Http Request
r = requests.get(url, headers=headers)
r.raise_for_status()

cards = r.json()

assert len(cards) > 0

# Saving cards into database
with transaction.atomic():
    card_list = []
    for card in cards:
        # Drop two cards that does not have a class "TRL_390e" and "TRL_085e"
        if "playerClass" in card:
            card_id = card["cardId"]
            dbf_id = card["dbfId"]
            name = card["name"]
            card_set = card["cardSet"]
            card_type = card["type"]
            player_class = card["playerClass"]
            collectible = True if "collectible" in card else False

            card_list.append(
                Cards(
                    card_id=card_id,
                    dbf_id=dbf_id,
                    name=name,
                    card_set=card_set,
                    card_type=card_type,
                    player_class=player_class,
                    collectible=collectible,
                )
            )

    Cards.objects.bulk_create(card_list)
