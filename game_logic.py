import random

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    max_mistakes = len(STAGES) - 1
    # Display the snowman stage for the current number of mistakes.
    print("-" * 30)
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Wort:   ", display_word)
    print("Fehler: ", f"{mistakes}/{max_mistakes}")
    print("-" * 30)


def play_game():
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        print("Welcome to Snowman Meltdown!")

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)

            if all(letter in guessed_letters for letter in secret_word):
                print("Gewonnen! Du hast den Schneemann gerettet.")
                break

            if mistakes >= max_mistakes:
                print("Verloren! Der Schneemann ist geschmolzen. Das Wort war:", secret_word)
                break

            guess = input("Guess a letter: ").lower()

            if guess in secret_word:
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
            else:
                mistakes += 1

        again = input("Nochmal spielen? (j/n): ").lower()
        if again != "j":
            print("Danke fuers Spielen!")
            break
