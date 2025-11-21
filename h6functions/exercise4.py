from random import randint


def roll_dice(number_dice):
    dice_list = []

    while len(dice_list) != number_dice:
        x = randint(1, 6)
        dice_list.append(x)
    return dice_list

question_answer = int(input("How many dices you want to work with: "))
dice = roll_dice(question_answer)
dice_count = 1

while len(dice) != dice.count(dice[0]):
    dice = roll_dice(question_answer)
    dice_count += 1

print(dice)
print(f"After {dice_count} roles we got a poker!")