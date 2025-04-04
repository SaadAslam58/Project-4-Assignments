def main():
    user_input1: int = int(input("Please enter an integer to be divided: "))
    user_input2: int = int(input("Please enter an integer to be divided: "))

    division = user_input1 // user_input2
    remainder = user_input1 % user_input2

    print(f"\nThe division of {user_input1} by {user_input2} is {division} with a remainder of {remainder}.\n")

if __name__ == '__main__':
    main()