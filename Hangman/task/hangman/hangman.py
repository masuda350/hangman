import random


def set_choices(word_list):
    return random.choice(word_list)


def hint(chosen_word, number_letters_shown):
    print('Guess the word {0}{hyphen}:'.format(chosen_word[:number_letters_shown],
                                               hyphen='-' * (len(chosen_word[number_letters_shown:]))))


def check_word(user_choice, chosen_word):
    print('You survived!' if user_choice == chosen_word else 'You lost!')


def show_remaining_letters(user_choice, chosen_letters, chosen_word):
    if user_choice in chosen_word:
        for i in range(len(chosen_word)):
            if user_choice == chosen_word[i]:
                chosen_letters[i] = user_choice
    else:
        print("That letter doesn't appear in the word")
    return chosen_letters


def start_message():
    print('H A N G M A N', '\n')


def end_message():
    print("Thanks for playing!")
    print("We'll see how well you did in the next stage")


def start_hangman(word_list):
    start_message()
    chosen_word = set_choices(word_list)
    chosen_letters = list('-' * len(chosen_word))
    for _ in range(8):
        print(''.join(chosen_letters))
        user_choice = input('Input a letter: ')
        chosen_letters = show_remaining_letters(user_choice, chosen_letters, chosen_word)
        print()

    end_message()


start_hangman(['python', 'java', 'kotlin', 'javascript'])
