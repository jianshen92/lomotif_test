from django.db import models
from djchoices import ChoiceItem, DjangoChoices


# Create your models here.
class Cards(models.Model):
    class CardClass(DjangoChoices):
        Druid = ChoiceItem("Druid")
        Hunter = ChoiceItem("Hunter")
        Mage = ChoiceItem("Mage")
        Paladin = ChoiceItem("Paladin")
        Priest = ChoiceItem("Priest")
        Rogue = ChoiceItem("Rogue")
        Shaman = ChoiceItem("Shaman")
        Warlock = ChoiceItem("Warlock")
        Warrior = ChoiceItem("Warrior")
        Neutral = ChoiceItem("Neutral")

    card_id = models.TextField(primary_key=True)
    dbf_id = models.TextField()
    name = models.TextField(help_text="Card's Name")
    card_set = models.TextField(help_text="Card's Expansion Set")
    type = models.TextField(help_text="Card's Type")
    player_class = models.TextField(choices=CardClass.choices)
    collectible = models.BooleanField(
        help_text="Whether the card is collectible. "
        "Collectible means able to build a standard deck with this card"
    )
