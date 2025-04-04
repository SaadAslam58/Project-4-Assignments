
HEIGHT: int = 10
def main():
    while True:
        user_input = input("How tall you are: ")
        if user_input == "":
            break

        height = float(user_input)
        if height >= HEIGHT:
            print(f"You are tall enough to ride!, leave it empty if want to exit.")
        else:
            print(f"You are not tall enough to ride, leave it empty if want to exit.") 


if __name__ == '__main__':
    main()