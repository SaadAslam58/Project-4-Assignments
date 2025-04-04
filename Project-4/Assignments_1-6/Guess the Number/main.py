import random

print("\n🎯 Welcome to Guess the Number! Try to guess the correct number.\n")

number = random.randint(1, 100)


while True:
    guess = int(input("Enter  a number: "))

    if (guess < number):
        print("⬇️ Too low!, Try again")
    elif (guess > number):
        print("⬆️ Too high!, Try again")
    else:
        print(f"\n🎉 Congratulations! You guessed the correct number {number}\n")
        break
