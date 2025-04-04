AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    user_input = input()
    while user_input != AFFIRMATION:
        print("Please retype the following input: " + AFFIRMATION)
        user_input = input()
    print("Congratulations! You have successfully typed the affirmation.")



if __name__ == '__main__':
    main()