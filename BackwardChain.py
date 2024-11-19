import random

stood = False
dealerStood = False

playerCard1 = random.randint(1,10)
playerCard2 = random.randint(1,10)
print("Your cards are ", playerCard1, playerCard2)
playerTotal = playerCard1 + playerCard2
print("Your total is", playerTotal)

dealercard1 = random.randint(1,10)
print("Dealer card is ", dealercard1)

while not stood:
    if playerTotal <= 21:
        if playerTotal >= 17:
            print("stand")
            stood = True
        elif playerTotal <= 11:
            print("hit")
            playerCard3 = random.randint(1,10)
            print("card is" , playerCard3)
            playerTotal = playerTotal + playerCard3
            print("total is", playerTotal)
        elif 11 < playerTotal < 17:
            if dealercard1 < 7:
                print("hit")
                playerCard4 = random.randint(1,10)
                print("card is" , playerCard4)
                playerTotal = playerTotal + playerCard4
                print("total is" , playerTotal)
            else:
                print("stand")
                stood = True
    else:
        print("bust")
        stood = True

dealercard2 = random.randint(1,10)
dealerTotal = dealercard1 + dealercard2
print("Dealers total is ", dealerTotal)

while not dealerStood:
    if dealerTotal <= 21:
        if dealerTotal > 17:
            print("stand")
            dealerStood = True
        else:
            print("hit")
            dealercard3 = random.randint(1,10)
            dealerTotal = dealerTotal + dealercard3
            print("Dealer total is ", dealerTotal)
    else:
        print("bust")

if playerTotal > 21 >= dealerTotal:
    print("dealer wins")
elif playerTotal <= 21 < dealerTotal:
    print("player wins")
elif playerTotal == dealerTotal:
    print("dealer wins")
elif dealerTotal < playerTotal <= 21:
    print("player wins")
elif playerTotal < dealerTotal <= 21:
    print("dealer wins")

