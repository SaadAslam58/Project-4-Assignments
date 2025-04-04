import random
max_value: int = 100
min_value: int = 0
n_value: int = 10
def main():
    for i in range(min_value, n_value):
        value = random.randint(min_value, max_value)
        i = value
        print(i)
     

if __name__ == '__main__':
    main()