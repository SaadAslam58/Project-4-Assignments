def main():
    lst: list = []
    user_input = input("Please enter a value: ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter another value (or press Enter to stop): ")
    
    print(f"The list contains {lst} elements.")


if __name__ == '__main__':
    main()