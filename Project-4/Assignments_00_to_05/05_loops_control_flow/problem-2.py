MAX_VALUE = 10000

def main():
    curr_value = 0
    next_value = 1
    while curr_value < MAX_VALUE:
        print(curr_value)
        total_value = curr_value + next_value
        curr_value = next_value
        next_value = total_value



if __name__ == '__main__':
    main()