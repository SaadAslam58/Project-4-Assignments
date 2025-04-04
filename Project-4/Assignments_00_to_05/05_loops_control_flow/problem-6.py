def main():
    user_input = int(input("Enter a number: "))
    print("Noted that:", user_input)
    while user_input < 100:

        doubled = user_input * 2
        user_input = doubled
        print(f"{user_input} doubled {doubled}")
    print("Any value greater then 100 will be the last value.")
    print(f"We stop at {user_input} because that value is greater than 100.")




if __name__ == '__main__':
    main()