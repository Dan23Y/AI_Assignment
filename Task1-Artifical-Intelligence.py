import pandas as pd
import random

playing = True

card1 = random.randint(1,10)
card2 = random.randint(1,10)
print("Your cards are: ", card1,"and",card2)
dealercard = random.randint(1,10)
cardTotal = card1 + card2

while playing:
    if cardTotal >= 17:
        print("Stand")
        playing = False
    elif cardTotal >= 11:
        print("hit")
        card3 = random.randint(1,10)
        cardTotal = cardTotal + card3
    elif 11 >= cardTotal >= 16:
        if dealercard >= 7:
            print("hit")
            card3 = random.randint(1,10)
            cardTotal = cardTotal + card3

