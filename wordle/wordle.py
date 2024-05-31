import random
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

def generate_word(infile='words.txt'):
    with open(infile) as file:
        content = file.read()
    lines = content.splitlines()
    line_number = random.randrange(0, len(lines))
    return lines[line_number]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def right(letter):
    return f"{Fore.WHITE}{Back.GREEN}{letter}{Style.RESET_ALL}"

def semi(letter):
    return f"{Fore.WHITE}{Back.YELLOW}{letter}{Style.RESET_ALL}"

def wrong(letter):
    return f"{Fore.WHITE}{Back.LIGHTBLACK_EX}{letter}{Style.RESET_ALL}"

def check_letters(word, user_guess):
    min_length = min(len(word), len(user_guess))
    results = ''

    for i in range(min_length):
        if user_guess[i] == word[i]:
            results += right(user_guess[i])
        elif user_guess[i] in word:
            results += semi(user_guess[i])
        else:
            results += wrong(user_guess[i])

    if len(word) > len(user_guess):
        for letter in word[len(user_guess):]:
            results += wrong(letter)
    elif len(word) < len(user_guess):
        for letter in user_guess[len(word):]:
            results += wrong(letter)

    return results

def main():
    word = generate_word()
    print("Word to guess:", word)  # Display the word the user is trying to guess
    input("Press Enter to start guessing...")

    attempts = 6
    guesses = []
    results = []
    previous_letters = []

    for i in range(attempts):
        clear_screen()
        print("Previous guesses:")
        for j, guess in enumerate(guesses):
            if i > 0:
                print(previous_letters[j])

        if i == 0:
            print("\nNo previous guesses yet!")

        print("\nGuess the word:")
        user_guess = input("Enter the guess: ").lower()
        user_guess2 = len(user_guess)

        # Check if the user provided a non-empty input
        if not user_guess:
            print("Please enter a guess.")
            input("Press Enter to continue...")
            attempts = +1
            continue

        elif user_guess2 < 5:
            print("Please enter a guess.")
            input("Press Enter to continue...")
            attempts = +1
            continue

        elif user_guess2 > 5:
            print("Please enter a guess.")
            input("Press Enter to continue...")
            attempts = +1
            continue

        guesses.append(user_guess)
        colored_guess = check_letters(word, user_guess)
        previous_letters.append(colored_guess)

        if user_guess == word:
            results.append("Right")
            break
        else:
            results.append("Wrong")

        if i < 5 and user_guess == word:  # Break early if the word is guessed correctly within 6 attempts
            results.append("Right")
            break

    clear_screen()
    print("Game Results:")
    if "Right" in results:
        print("Congratulations! You guessed the word!")
    else:
        print("Sorry, you failed to guess the word. | " + word)

    print("\nPrevious guesses:")
    for j in range(len(guesses)):  # Skip the first guess which is the randomly generated word
        print(previous_letters[j])

if __name__ == "__main__":
    main()


