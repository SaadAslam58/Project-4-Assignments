def main():
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    sum_of_sides = side1 + side2 + side3

    print(f"\nSides of triangle are {side1}, {side2}, {side3} and\n The perimeter of the triangle is '{sum_of_sides}'.\n")

if __name__ == '__main__':
    main()