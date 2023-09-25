"""EX02 - One Shot Wordle - The New York Times is getting nervous (satire)."""

__author__ = "730529193"
# secret word, boolean operators to assess guesses (and emoji strings) and end loops, idx value (for Green) and alt_idx value (for yellow and white), input prompt str, and emoji values.
scrt_word = "python"
correct_guess = True
idx = 0
alt_idx = 0
char_exists = False
emoji = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_word: str = input(f"What is your {len(scrt_word)}-letter guess? ")
# while the value is true if the length of the guess is unequal to the length of the secret word provide new input until a proper guess is made (initialize to true), the print values for elif and else had to be moved in order to display after the emoji
while correct_guess:
    if len(guess_word) != len(scrt_word):
        guess_word = input(f"That was not {len(scrt_word)} letters! Try again: ")
        correct_guess = True
    elif guess_word == scrt_word:
        correct_guess = False
    else:
        correct_guess = False
# if the index of the guess word is matched to the index of the secret word then the green_box will be stored for the instances also initizialing the value for if the character exists within the word.
while idx < len(scrt_word):
    if guess_word[idx] == scrt_word[idx]:
        emoji += GREEN_BOX
    else:
        char_exists = False
        alt_idx = 0
# if letters of the guessword exist in scrt_word but at the wrong index then each index will be checked and a yellow box will be stored for those instances
        while not char_exists and alt_idx < len(scrt_word):
            if scrt_word[alt_idx] == guess_word[idx]:
                char_exists = True
            else: 
                alt_idx += 1
# if the character exists within the scrt_word but at the wrong index print a yellow box if not print a white box and don't create extra boxes     
        if char_exists:
            emoji += YELLOW_BOX
        else: 
            emoji += WHITE_BOX

    idx += 1

print(emoji)
# display code for the first while loop code
if guess_word == scrt_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

















