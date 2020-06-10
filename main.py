import random

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds != 6:
        print("Runda " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Igrac 1 baca : " + str(player1))
        print("Igrac 2 baca : " + str(player2))

        if player1 == player2:
            print("Nereseno!")
        elif player1 > player2:
            print("Igrac 1 pobedjuje!\n")
            player1wins = player1wins + 1
        else:
            print("Igrac 2 pobedjuje!\n")
            player2wins = player2wins + 1

        rounds = rounds + 1

    print("Igrac 1 ukupno pobeda : " + str(player1wins))
    print("Igrac 2 ukupno pobeda : " + str(player2wins))

    if player1wins == player2wins:
        print(" Nereseno je !!! Nema pobednika " )
    elif player1 > player2:
        print("Igrac 1 ima vise pobeda u ukupno bacanja")
    else:
        print("Igrac 2 ima vise pobeda u ukupno bacanja")

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()


