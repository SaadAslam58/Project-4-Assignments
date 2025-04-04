import random
def main():
    secret_random = random.randint(1, 99)
    while True:
        user_input = int(input("Enter a random number: "))
        if user_input == secret_random:
            print("Congratulation you won the game!.")
            break
        
        if user_input < secret_random:
            print("Too low, guess higher.")
        else:
            print("Too high, guess lower.")
            print()

    print("The number you have guessed " + str(user_input) + " and computer's number " + str(secret_random))



if __name__ == '__main__':
    main()