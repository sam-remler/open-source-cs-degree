import string
import random

all_letters = list(string.ascii_lowercase)

def has_player_won(secret_word : str, letters_guessed : list[str]) -> bool:
    """ returns True if all user has guessed all the letters in a secret word. False otherwise"""

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word : str, letters_guessed : list[str]):
    """ returns the revealed letters in a secret word based on the letters guessed so far"""

    revealed_text = ""
    for letter in secret_word:
        if letter in letters_guessed:
            revealed_text += letter
        else:
            revealed_text += "*"
    return revealed_text

def get_available_letters(letters_guessed : list[str]):
    available_letters = all_letters.copy()
    for letter in letters_guessed:
        available_letters.remove(letter)
    return "".join(available_letters)
    
def choose_letter(secret_word, available_letters):
    secret_letters = list(set(list(secret_word)))
    secret_letters = [letter for letter in secret_letters if letter in available_letters]


    revealed_letter = random.choice(secret_letters)
    return revealed_letter

def line_break():
    print ("----------------------------\n")


def hangman(secret_word : str, with_help : bool):
    print ("Welcome to Hangman!")
    print (f"I'm thinking of a word that is {len(secret_word)} letters long.")
    line_break()

    guesses_left = 10
    letters_guessed = []
    progress = get_word_progress(secret_word, letters_guessed)
    while (not has_player_won(secret_word, letters_guessed)) and (guesses_left != 0):
        print (f"You have {guesses_left} guesses left.")
        print (f"Available letters: {get_available_letters(letters_guessed)}")
        
        new_guess = input("Please guess a letter: ")
        
        if new_guess == "!":
            if not with_help:
                print ("You are playing with help off. That is not a valid letter. Please input a letter from the alphabet:")
            elif guesses_left < 3:
                print ("You don't have enough guesses for a hint.")
            else:
                revealed_letter = choose_letter(secret_word, get_available_letters(letters_guessed))
                print(f"Letter revealed: {revealed_letter}")
                letters_guessed.append(revealed_letter)
                print(get_word_progress(secret_word, letters_guessed))
                guesses_left -= 3

        elif (not new_guess.isalpha()) or (len(new_guess) > 1) or (new_guess.lower() not in all_letters):
            print (f"Oops! That is not a valid letter. Please input a letter from the alphabet: {progress}")

        elif new_guess.lower() in letters_guessed:
            print (f"Oops! You've already guessed that letter: {progress}")

        elif new_guess.lower() in secret_word:
            letters_guessed.append(new_guess.lower())
            progress = get_word_progress(secret_word, letters_guessed)
            print (f"Good guess: {progress}")

        elif new_guess.lower() in ['a', 'e', 'i', 'o', 'u']:
            letters_guessed.append(new_guess.lower())
            print (f"Oops! That letter is not in my word: {progress}")
            guesses_left -= 2

        else:
            letters_guessed.append(new_guess.lower())
            print (f"Oops! That letter is not in my word: {progress}")
            guesses_left -= 1
        
        line_break()
    
    if guesses_left == 0:
        print (f"Sorry, you ran out of guesses. The word was {secret_word}.")
    else:
        print (f"Congratulations, you won!")
        total_score = guesses_left + 4 * len(set(list(secret_word))) + (3*len(secret_word))
        print (f"Your total score was {total_score}")

  

if __name__ == "__main__":
    with open("words.txt","r") as file:
        content = file.read()
        
    words = content.split(" ")
    secret_word = random.choice(words)

    hangman(secret_word, True)