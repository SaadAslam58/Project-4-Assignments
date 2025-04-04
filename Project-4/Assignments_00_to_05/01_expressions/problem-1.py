import random

num_sides = 6
def roll_dice():

    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)

    total = die1 + die2

    print(f"You rolled a {die1} and a {die2}. The total is {total}.")

def main():
    print("Welcome to the dice roller!")
    roll_dice()
    roll_dice()
    roll_dice()

if __name__ == "__main__":
    main()