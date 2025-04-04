import random

words = ["cat", "dog", "bat"]
word = random.choice(words)
hidden = ["_"] * len(word)
lives = 5

while lives > 0 and "_" in hidden:
    print("\nWord:", " ".join(hidden))
    guess = input("Guess the letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
    else:
        lives -= 1
        print("Incorrect guess. Lives left: ", lives)

if "_" not in hidden:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nSorry, you lost. The word was: ", word)
