import random

Roll_Dice = 6
def main():
    user_input1: int = random.randint(1, Roll_Dice)
    user_input2: int = random.randint(1, Roll_Dice)
    sum_of_input: int = user_input1 + user_input2

    print("THe dice have",Roll_Dice,"sides")
    print("The number of 'Dice1' is " + str(user_input1))
    print("The number of 'Dice2' is " + str(user_input2))
    print("The total of both dices are " + str(sum_of_input))
if __name__ == '__main__':
    main()