import random

words = ["apple", "banana", "cherry", "grapes", "orange"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts_left = 6
used_letters = []

print("Welcome to Hangman!")

while attempts_left > 0 and "_" in guessed_word:
    print("\nWord so far:", " ".join(guessed_word))
    print("Used letters:", ", ".join(used_letters))
    print(f"Attempts left: {attempts_left}")

    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter. Try another one.")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess.")
        attempts_left -= 1

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)