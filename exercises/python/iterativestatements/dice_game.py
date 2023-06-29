import random


def dice_game():
    first_wins = second_wins = 0
    while first_wins < 1000 and second_wins < 1000:
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        if first_dice > second_dice:
            first_wins += 1
        if first_dice < second_dice:
            second_wins += 1
    print('first player won') if first_wins == 1000 else print('second player won')
