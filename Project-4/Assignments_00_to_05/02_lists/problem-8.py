MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)

def get_lst():
    lst = []
    user_input = input("Please enter an element of the list or press enter to stop. ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == "__main__":
    main()