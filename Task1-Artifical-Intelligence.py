import random

playing = True
dealerplay = True

card1 = random.randint(1,10)
card2 = random.randint(1,10)
print("Your cards are: ", card1,"and",card2)
dealercard = random.randint(1,10)
print("The dealers card is ", dealercard)
cardTotal = card1 + card2
print("The total of players cards is" , cardTotal)

while playing:
    if cardTotal >= 17:
        print("Stand", cardTotal)
        playing = False
    elif cardTotal <= 11:
        print("hit")
        card3 = random.randint(1,10)
        cardTotal = cardTotal + card3
        print(cardTotal)
    elif 11 <= cardTotal <= 16:
        if dealercard >= 7:
            print("hit")
            card3 = random.randint(1,10)
            cardTotal = cardTotal + card3
            print(cardTotal)
        else:
            print("stand")
            playing = False
    elif  cardTotal > 21:
        print("bust")
        playing = False

dealercard2 = random.randint(1,10)
dealerTotal = dealercard2 + dealercard
print("The dealers card is ", dealercard2)
print("The dealers total is", dealerTotal)
while dealerplay:
    if dealerTotal > 21:
        print("bust")
        dealerplay = False
    elif dealerTotal < 17:
        print("hit")
        dealercard3 = random.randint(1,10)
        dealerTotal = dealerTotal + dealercard3
    elif 17 <= dealerTotal <= 21:
        print("stand")
        print(dealerTotal)
        dealerplay = False

if dealerTotal == 21 and cardTotal == 21:
    print("The dealer Wins")
elif cardTotal < 22 and cardTotal > dealerTotal:
     print("player wins")
elif dealerTotal < 22 and dealerTotal > cardTotal:
    print("The dealer Wins")
elif cardTotal > 21 and dealerTotal > 21:
    print("both bust")