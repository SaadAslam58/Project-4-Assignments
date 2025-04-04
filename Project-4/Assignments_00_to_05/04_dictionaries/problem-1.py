def get_user_number():
    user_number = []
    while True:
        user_input = input("Enter a key and value: ")

        if user_input == "":
            break

        number = int(user_input)
        user_number.append(number)

    return user_number

def count_number(num_lst):
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1

        else:
            num_dict[num] = 1
    
    return num_dict

def print_count(num_dict):
    for num in num_dict:
        if num in num_dict:
            print(str(num) + " appears " + str(num_dict[num]) + " times.")
    
def main():
    user_number = get_user_number()
    num_dict = count_number(user_number)
    print(num_dict)


if __name__ == "__main__":
    main()




