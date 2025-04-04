Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

def main():
    your_age = int(input("Enter your age: "))
    if your_age >= Peturksbouipo:
        print(f"You can vote in Peturksbouipo")
    else:
        print("You are not old enougth to vote.")
    if your_age >= Stanlau:
        print(f"You can vote in Stanlau")
    else:
        print("You are not old enougth to vote.")
    if your_age >= Mayengua:
        print(f"You can vote in Mayengua")
    else:
        print("You are not old enougth to vote.")


if __name__ == '__main__':
    main()