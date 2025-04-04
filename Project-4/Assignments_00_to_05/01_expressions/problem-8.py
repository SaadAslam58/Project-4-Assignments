def main():
    print("\nWelcome to our tiny mad libs game!\n")
    user_adjective = str(input("Please enter an adjective: "))
    user_noun = str(input("Please enter an noun: "))
    user_verb = str(input("Please enter an verb: "))

    print(f"In a land far away, there lived a {user_adjective} {user_noun}. This {user_noun} was always {user_verb}ing, but today, he turned into a {user_adjective} {user_noun}.")

if __name__ == '__main__':
    main()