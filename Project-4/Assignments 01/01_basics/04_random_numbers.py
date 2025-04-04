import random
MAX_VALUE = 100
MIN_VALUE = 1
N_NUMBER = 10

def main():
    for num in range (MIN_VALUE, N_NUMBER):
        random_num = random.randint(MIN_VALUE, MAX_VALUE)
        num = random_num
        print(num, end=" ")
        
    # for i in range(0, 10):
    #     i = random.randint(MIN_VALUE, MAX_VALUE)
    #     print(i)

if __name__ == '__main__':
    main()
        