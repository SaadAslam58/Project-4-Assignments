import random

"""
0 = Rock
1 = Paper
2 = Scissors
"""

print("\nWelcome to Rock, Paper, Scissors!🎯\n")
name_input = input("Enter your name: ")
print("\n0 = Rock🪨, 1 = Paper📃, 2 = Scissors✂️\n")

user_input = int(input("Select one of the following: "))

comp_input = random.randint(0,2)
you_dict = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}
comp_dict = {
   0: "Rock",
    1: "Paper",
    2: "Scissors"   
}
you_choice = user_input

if you_choice == comp_input:
    print(f"\nIt's a tie!, both of you selected {comp_dict[comp_input]} \n")
else:
    if you_choice == 0 and comp_input == 1: 
        print(f"\nComputer chose {comp_dict[comp_input]} and you choose {you_dict[you_choice]}")
        print(f"\n{name_input} loose!🥹")
    if you_choice == 0 and comp_input == 2: 
        print(f"\nComputer chose {comp_dict[comp_input]}, and you choose {you_dict[you_choice]}")
        print(f"\n{name_input} wins!😁")
    if you_choice == 1 and comp_input == 0: 
        print(f"\nComputer chose {comp_dict[comp_input]}, and you choose {you_dict[you_choice]}")
        print(f"\n{name_input} wins!😁")
    if you_choice == 1 and comp_input == 2: 
        print(f"\nComputer chose {comp_dict[comp_input]}, and you choose {you_dict[you_choice]}")
        print(f"\n{name_input} loose!🥹")
    if you_choice == 2 and comp_input == 0: 
        print(f"\nComputer chose {comp_dict[comp_input]}, and you choose {you_dict[you_choice]}")
        print(f"\n{name_input} loose!🥹")
    if you_choice == 2 and comp_input == 1: 
        print(f"\nComputer chose {comp_dict[comp_input]}, and you choose {you_dict[you_choice]}")
        print(f"{name_input} wins!😁")
    
    