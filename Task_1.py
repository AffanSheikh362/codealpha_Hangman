import random

# Hangman stages
hangman_stages = [
    '''
      -----
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    '''
]

def hangman():
    words = ['python', 'java', 'affan', 'javascript']
    word = random.choice(words)
    guessed_word = ['_' for _ in word]
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))
    print(hangman_stages[0])

    while attempts > 0 and '_' in guessed_word:
        guess = input("\nGuess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            print("Good guess!")
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f"Incorrect! You have {attempts} attempts left.")

        print(" ".join(guessed_word))
        print(hangman_stages[6 - attempts])
        print("The above Hangman diagram visually represents the progress of the game and the player's remaining attempts")
    if '_' not in guessed_word:
        print("\nCongratulations! You've won!")
    else:
        print(f"\nSorry, you've lost. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
