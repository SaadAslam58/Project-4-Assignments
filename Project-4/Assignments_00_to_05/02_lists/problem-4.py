def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    user_input = input("Enter a word or anything: ")
    my_list = []
    print("Before", my_list)
    add_three_copies(my_list, user_input)
    print("After", my_list)


if __name__ == '__main__':
    main()
