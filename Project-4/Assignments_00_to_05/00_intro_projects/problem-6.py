def main():
    user_input = float(input("Enter a number to get a square of it: "))

    square_number = user_input**2

    print(f"\nThe square of {user_input} is {square_number}.\n")


if __name__ == '__main__':
    main()