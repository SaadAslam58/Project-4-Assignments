def main():
    user_input = int(input("Input a temperature in fahrenheit: "))
    celsius = (user_input - 32) * 5.0/9.0
    print(f"{user_input:.2f}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    main()