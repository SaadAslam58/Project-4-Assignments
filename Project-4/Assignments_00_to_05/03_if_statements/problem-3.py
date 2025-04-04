def main():
    user_input = int(input("Please enter a year: "))
    if user_input % 4 == 0:
        if user_input % 100 == 0:
            if user_input % 400 == 0:
                print(f"{user_input} is a leap year.")
            else:
                print(f"{user_input} is not a leap year.")
        else:
            print(f"{user_input} is a leap year.")
    else:
        print(f"{user_input} is not a leap year.")



if __name__ == '__main__':
    main()