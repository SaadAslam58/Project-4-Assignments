import random

def main():
    print("\nWelcome to High-Low Game!")
    total_score = 0
    total_round = 0
    end_round = 5

    while total_round < end_round:
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)

        print(f"\nYour generated number is '{your_number}'")
        user_input = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        if your_number == computer_number:
            print(f"Your number {your_number} and computer number {your_number} is same.")
            print(f"Computer has won!")
            break

            
        if your_number > computer_number and user_input == "higher":
            total_round += 1
            print(f"\nRound {total_round}")
            print(f"Your number is '{your_number}'")
            print(f"Your guess was correct, computer number is lower {computer_number}")
            total_score += 1
            print(f"Your score is {total_score}")

        elif your_number < computer_number and user_input == "lower":
            total_round += 1
            print(f"Round {total_round}")
            print(f"Your guess was correct, computer number is higher {computer_number}")
            total_score += 1
            print(f"Your score is {total_score}")


        elif your_number > computer_number and user_input == "lower":
            total_round += 1
            print(f"Round {total_round}")
            print(f"Your guess was incorrect, computer number is lower {computer_number}")
            print(f"Your score is {total_score}")

        elif your_number < computer_number and user_input == "higher":
            total_round += 1
            print(f"Round {total_round}")
            print(f"Your guess was incorrect, computer number is higher {computer_number}")
            print(f"Your score is {total_score}")
        
    if total_score == 1:
                print(f"\nBetter luck next time!, your score is {total_score}")
    elif total_score == 2:
                print(f"\nCongratulations!, your score is {total_score}")
    elif total_score == 3:
                print(f"\nGood job, you played really well!, your score is {total_score}")
    elif total_score == 4:
                print(f"\nWell played, your score is {total_score}")
    elif total_score == 5:
                print(f"\nWow! You played perfectly!, your score is {total_score}")


if __name__ == "__main__":
    main()