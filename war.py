import random

# Define the deck of cards
deck = [i for i in range(1, 14)] * 4
random.shuffle(deck)

# Split the deck between two players
player1 = deck[:26]
player2 = deck[26:]

while player1 and player2:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1 > card2:
        player1.extend([card1, card2])
    elif card2 > card1:
        player2.extend([card1, card2])
    else:
        # War condition: each player puts down three cards, and the third one decides who wins
        if len(player1) < 4 or len(player2) < 4:
            # If a player doesn't have enough cards to play the war, they lose
            player1 = player1 if len(player1) > len(player2) else []
            break

        cards1 = [player1.pop(0) for _ in range(3)]
        cards2 = [player2.pop(0) for _ in range(3)]

        if cards1[-1] > cards2[-1]:
            player1.extend(cards1 + cards2)
        else:
            player2.extend(cards1 + cards2)

# Determine the winner
if player1:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
