# # Task 4: Closure Practice

# # Task 4: step 2
# Declare a function called make_hangman() that has one argument called secret_word
def make_hangman(secret_word):
    # declare an empty array called guesses
    guesses = []

    # declare a function called hangman_closure() that takes a letter
    def hangman_closure(letter):
        #  appended the new letter to the guesses array
        guesses.append(letter.lower())

        display_word = ""
        all_guessed = True

        # build display string with the current guesses
        for char in secret_word.lower():
            if char in guesses:
                display_word += char
            else:
                display_word += "_"
                all_guessed = False
                
        print(display_word)
        return all_guessed
            
    return hangman_closure

# Task 4: step 3
# Implement a hangman game that uses make_hangman()
if __name__ == "__main__":

    #  Use the input() function to prompt for the secret word
    secret = input("Enter the secret word: ").strip()

    play_round = make_hangman(secret)
    
    is_finished = False
    print("\nGame started!")


    # use the input() function to prompt guesses until the full word is guessed
    while not is_finished:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) == 1 and guess.isalpha():
            is_finished = play_round(guess)
        else:
             print("Invalid input. Please enter exactly one letter.")

    # Task 4: step 4
    print("Great! You have guessed the full word")
