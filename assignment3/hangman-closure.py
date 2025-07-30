def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter.lower())
        
        result = ""

        for ch in secret_word:
            if ch.lower() in guesses:
                result += ch
            else:
                result += "_"

        print(result)

        for ch in secret_word:
            if ch not in guesses:
                return False
            
        return True
    return hangman_closure

if __name__ == "__main__":
    word = input("Enter a secret word: ")
    hangman = make_hangman(word)

    while True:
        guess = input("Guess a letter: ")

        if hangman(guess):
            print(f'You guessed the word: {word}')
            break