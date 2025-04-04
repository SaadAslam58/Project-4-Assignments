import random

def main():
    my_guess = random.randint(0, 100)

    while True:
        user_input = input("Enter a number or (leave it empty to exit): ")
        if user_input == "":
            print("Goodbye!")
            break

        user_input = int(user_input)
        if user_input < my_guess:
            print("Too low, guess higher.")
        elif user_input == my_guess:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Too high, guess lower.")


    
    


if __name__ == "__main__":
    main()
