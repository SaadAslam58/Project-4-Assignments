import math
def main():
    user_input1: float = float(input("\nEnter the length of side AB: "))
    user_input2: float = float(input("Enter the length of side AC: "))
    hypotenuses: float = math.sqrt(user_input1 **2 + user_input2 **2) # C = sqrt(A**2 + B**2)
    print(f"\nThe length of side BC (the hypotenuses) is {hypotenuses}\n")
    

if __name__ == '__main__':
    main()