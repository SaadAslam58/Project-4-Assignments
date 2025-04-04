MAX_VALUE = 100 
def main():
    user_input = int(input("Enter a number: "))
    print(f"Noted {user_input}")
    while user_input < MAX_VALUE:
        pre_value = user_input
        curr_value = user_input * 2
        user_input = curr_value
        
        print(f"{pre_value} doubled {user_input}")
        
    print(f"Once the number exceed 100, it will be its last value.")

 
if __name__ == '__main__':
    main()