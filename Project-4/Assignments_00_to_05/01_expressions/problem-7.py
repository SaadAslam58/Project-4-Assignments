Days = 365
Hour = 24
Minute = 60
Second = 60

def main():

    total_year_seconds = Days * Hour * Minute * Second

    print("There are " + str(Days) + " days " + str(Hour) + " hours " + str(Minute) + " mins " + str(Second) + " seconds in a year")

if __name__ == '__main__':
    main()