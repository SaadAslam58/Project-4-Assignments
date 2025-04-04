def access_element(lst, index):
    try:
        return lst[index]
    except:
        return "Index out of reach."

def update_element(lst, index, value):
    try:
        lst[index] = value
    except:
        "Index out of reach."
def append_element(lst, value):
    try:
        lst.append(value)
    except:
        "Index uut of reach." 
def delete_element(lst, index):
    try:
        del lst[index]
        return lst
    except:
        "Index out of reach."

def reverse_element(lst):
    return lst[::-1]

def slice_element(lst, start, end):
    try:
        return lst[start:end]
    except:
        "Index out of reach."

def main():
    print("\nGame start!!!\n")
    lst = [1, "orange", 3.141, "apple", "grapes"]
    print("""\nSelect one of the operation to perform\n
    1. Access elements
    2. Update elements
    3. Append elements
    4. Delete elements
    5. Reverse elements
    6. Slice elements
    \n""")
    user_input = input("Enter an operation: ").strip().lower()
    if user_input == "access":
        index = int(input("Enter an index to access: "))
        result = access_element(lst, index)
        print(f"\nThe value in index {index} is '{result}': {lst}")
    elif user_input == "update":
        index = int(input("Enter an index to access: "))
        value = input("Enter the new value: ")
        result = update_element(lst, index, value)
        print(f"\nThe value at index {index} is updated to '{value}': {lst}")
    elif user_input == "delete":
        index = int(input("Enter an index to delete: "))
        result = delete_element(lst, index)
        print(f"\nThe value at index {index} is now deleted: {lst}")
    elif user_input == "append":
        value = input("Enter an value to append: ")
        result = append_element(lst, value)
        print(f"\nThe value '{value}' is appended: {lst}")
    elif user_input == "reverse":
        old_list = lst
        lst = reverse_element(lst)
        print(f"\nNew list: {lst}\nOld list: {old_list}")
    elif user_input == "slice":
        start = int(input("Enter the first index: "))
        end = int(input("Enter the next index: "))
        result = slice_element(lst, start, end)
        print(f"\nThe list is now sliced from index {start} to {end}: {result}")

    
if __name__ == "__main__":
    main()

    
