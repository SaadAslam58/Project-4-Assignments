import random 

print("\n🤔Think of a number computer will try to guess it🎯\n")

low = 0
high= 20
attempts = 1

user_number = int(input("Your guessed number: "))

while True:
    comp_guess = random.randint(low,high) 
    print(f"\nThe number I have guess is {comp_guess} and its my {attempts} attempts\n")
    feedback = input("If the number is right say 'yes': ").lower()
    attempts += 1

    if feedback == "yes":
        print(f"\n💥Congratulations you have won the game!🚀 {user_number}\n")
        break
    elif feedback == "high":
        print("\n⬆️  Too high, try again")
        comp_guess = -1
    elif feedback == "low":
        print("\n⬇️  Too low, try again")
        comp_guess = +1

    