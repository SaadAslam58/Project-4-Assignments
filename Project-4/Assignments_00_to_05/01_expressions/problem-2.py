def main():
    mass_input = float(input("Enter a value of mass in (kg): "))
    speed_of_light = 299792458 
    total_energy = mass_input * speed_of_light**2
    print(f"The value of mass = {mass_input} kg\nC = {speed_of_light} m/s\nE = {total_energy} joules")



if __name__ == '__main__':
    main()