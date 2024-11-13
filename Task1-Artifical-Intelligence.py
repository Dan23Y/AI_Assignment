import pandas as pd

data = pd.read_csv("blackjack.csv")

def blackJackForward(playerTotal, DealerCard, playerCards):
    if playerTotal >= 17:
        return "stand"
    elif playerTotal >= 11:
        return "hit"
    elif playerTotal == 11 and DealerCard < 10:
        return "double down"
    elif playerTotal in [11, 12, 13, 14, 15, 16] and DealerCard >= 7:
        return "hit"
    elif playerTotal == 10 and DealerCard < 10:
        return "double down"
    elif len(playerCards) == 2 and playerCards[0] == playerCards[1]:
        if playerCards[0] in [8, 11]:
            return "split"
    return "stand"

action = blackJackForward(playerTotal, DealerCard ,playerCards)
print(f"The recommended action is: {action}")