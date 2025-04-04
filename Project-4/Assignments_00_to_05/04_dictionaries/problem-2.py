def read_number():
    phonebook = {}
    while True:
        user_name = input("Enter a name to store: ")
        if user_name == "":
            break
        user_number = input("Enter number: ")
        phonebook[user_name] = user_number

    return phonebook

def print_phonebook(phonebook):
    for user_name in phonebook:
        print(str(user_name) + " -> " + str(phonebook[user_name]))

def lookup_number(phonebook):
    while True:
        user_name = input("Enter a name to lookup: ")
        if user_name == "":
            break
        if user_name in phonebook:
            print(f"{user_name}'s number is {phonebook[user_name]}")
        if user_name not in phonebook:
            print(f"{user_name} not found in the phonebook.")
        else:
            print(phonebook[user_name])
        
def main():
    user_input = read_number()
    print_phonebook(user_input)
    lookup_number(user_input)

if __name__ == "__main__":
    main()

