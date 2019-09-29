from django.urls import path

from . import views

urlpatterns = [
    path("create_deck/<player_class>", views.create_deck, name="create_deck")
]
