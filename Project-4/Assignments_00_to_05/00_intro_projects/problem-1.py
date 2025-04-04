def main():
    user_input1: str = input("Enter a number: ")
    user_input2: str = input("Enter another number: ")

    number: int = int(user_input1) + int(user_input2)

    print(f"The sum of {user_input1} and {user_input2} = {number}")

if __name__ == "__main__":
    main()
