# Lomotif Backend Test

This repository is a submission for Lomotif's Backend Engineer Technical Test.

Table of Contents:
* [Overview](#overview)
* [API Endpoints](#api-endpoints)
* [Setting Up Locally](#setting-up-locally)
* [Note to Test Examiner](#note-to-test-examiner)

## Overview
This assignment provides a django-backend API endpoint to build a legitimate Hearthstone deck just by specifying a Hearthstone Class.
A legitimate deck has the following conditions:
1) The deck must contain only cards of a particular Class or “Neutral” Class.
2) There can only be a maximum of two of the same cards.
3) There are 30 cards in the deck

The deployed heroku server :
https://evening-stream-77471.herokuapp.com/

## API Endpoints
**Creating deck based on given Player Class**

`/cards/create_deck/<player_class>`

Slug argument:

**player_class** `str` : One of the follow Hearthstone classes. 
Druid, Hunter, Mage, Paladin, Priest, Rogue, Shaman, Warlock, Warrior

Example : `/cards/create_deck/Mage`

Sample response: 
```
[
    {
        "dbf_id": "53217", 
        "name": "Bananas", 
        "player_class": "Neutral"
    }
, 
    {
        "dbf_id": "50786", 
        "name": "Blessing of Halazzi", 
        "player_class": "Neutral"
    }
,
    {
        "dbf_id": "51808", 
        "name": "Jan'alai's Progeny", 
        "player_class": "Mage"
    }
    ...
]
```

Additional arguments:

**collectible** `Bool`: Filters out whethere the cards are collectible. 
(Not every card in Hearthstone expansions is collectible. To build a deck for standard gameplay, 
we can only build cards that is collectible.)

Example : `/cards/create_deck/Mage?collectible=True`

## Setting Up Locally
**Prerequisite**
1. Postgresql + the correct credentials and database initialized
2. Virtualenv (Python 3+)

**Installation**
1. Install dependencies `make install-requirements`
2. Database Migration `make migrate`
3. Populate database by running `make populate-db` once.
4. Run Development Server `make runserver`

## Note to Examiner
Thanks for giving me a chance to perform the test offline. 
Since I have the liberty of time to complete the test, I did some extra work to make the submission better.

**Exploration Data Analysis (EDA) with pandas**

I did some data exploration on the json data with pandas (see `Lomotif EDA.ipynb`) and discovered a few insights.
1. Some card information are present in some cards but not all. In the end I decided to only save the common card 
information in database.
2. There is a field called `collectible`. In hearthstone you can only build a deck with cards that is collectible.
Therefore I decided to include a query argument called `collectible`.
3. There are two cards with NaN Player Class. I decided to not save two of the cards to the database.

**Using formatters to format the codes**

I made use of some formatters like `black` and `isort` to format my code to adhere to PEP8 conventions.
We can run `make format` to run them.

