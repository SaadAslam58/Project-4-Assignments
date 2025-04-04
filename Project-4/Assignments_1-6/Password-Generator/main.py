import random

print("Welcome to 'Password Generator!'")

char = "abcdefghijklmnopqrstuvwxyzABCDEFINERRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter the length of the passowrd: "))

number = int(input("Enter the number of passowrd to be generated: "))

print("\nGenerated Passwords")

for pws in range(length):
    password = ""
    for c in range(number):
        password += random.choice(char)
    print(password)