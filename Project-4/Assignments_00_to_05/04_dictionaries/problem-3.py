def main():
    fruit_list = {
    'apple': 1,
    'banana': 2,
    'cherry': 3,
    'date': 4,
    'elderberry': 5,
    'fig': 6,
    }
 
    total = 0
    for fruit in fruit_list:
        price = fruit_list[fruit]
        user_input = int(input("How many " + (fruit) + " do you want to buy: "))
        total += (price * user_input)
        
    print("Your total is $" + str(total))




if __name__ == '__main__':
    main()