import random
from visual import hangman_visual

def choose_word():
    file_path = "/Path/to/words.txt"
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nAttempts left:", attempts)
        print(display_word(word_to_guess, guessed_letters))
        print(hangman_visual[attempts])

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print("Incorrect guess")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break

        if attempts == 0:
            print(hangman_visual[attempts])
            print("\nYou ran out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
