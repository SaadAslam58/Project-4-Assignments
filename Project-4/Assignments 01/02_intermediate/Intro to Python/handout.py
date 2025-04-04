MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0
def Earthling():
    print("Welcome to the Earthling Gravity Converter!")
    print("""Select a planet from the list below
    1. Mercury
    2. Venus
    3. Mars
    4. Jupiter
    5. Saturn
    6. Uranus
    7. Neptune
    8. Earth
    """)
    planet_list = str(input("\nSelect a planet from the given list: "))
    user_input = float(input("Now enter your weight: "))

    return user_input, planet_list

def convert_weight_earth(user_input, planet_list):
    if planet_list == "Mercury":
        weight_conversion = user_input * MERCURY_GRAVITY
    elif planet_list == "Venus":
        weight_conversion = user_input * VENUS_GRAVITY
    elif planet_list == "Mars":
        weight_conversion = user_input * MARS_GRAVITY
    elif planet_list == "Jupiter":
        weight_conversion = user_input * JUPITER_GRAVITY
    elif planet_list == "Saturn":
        weight_conversion = user_input * SATURN_GRAVITY
    elif planet_list == "Uranus":
        weight_conversion = user_input * URANUS_GRAVITY
    elif planet_list == "Neptune":
        weight_conversion = user_input * NEPTUNE_GRAVITY
    else:
        weight_conversion = user_input * EARTH_GRAVITY
    
    print(f"\nYour weight on {planet_list} would be approximately {weight_conversion:.2f}.\n")

    return weight_conversion 
    

def other_planet(user_input, weight_conversion):
    print(f"Would to like to convert your weight {weight_conversion:.2f} to other planets\n")
    planet_list =input("Enter your next planet to convert: ")
    if planet_list == "Mercury":
        new_weight = user_input * MERCURY_GRAVITY
    elif planet_list == "Venus":
        new_weight = user_input * VENUS_GRAVITY
    elif planet_list == "Mars":
        new_weight = user_input * MARS_GRAVITY
    elif planet_list == "Jupiter":
        new_weight = user_input * JUPITER_GRAVITY
    elif planet_list == "Saturn":
        new_weight = user_input * SATURN_GRAVITY
    elif planet_list == "Uranus":
        new_weight = user_input * URANUS_GRAVITY
    elif planet_list == "Neptune":
        new_weight = user_input * NEPTUNE_GRAVITY
    else:
        new_weight = user_input * EARTH_GRAVITY
        
    print(f"\nYour weight on {planet_list} would be approximately {new_weight:.2f}.\n")
    

if __name__ == "__main__":

    user_input, planet_list = Earthling()
    weight_conversion = convert_weight_earth(user_input, planet_list)
    other_planet(user_input, weight_conversion)


