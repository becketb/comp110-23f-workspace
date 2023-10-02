"""EX03 - Structured Wordle - Count your days The New York Times (satire)."""

__author__ = "730529193"

WHITE_BOX = "\U00002B1C"
GREEN_BOX = "\U0001F7E9"
YELLOW_BOX = "\U0001F7E8"


def contains_char(search_string: str, char_searched: str) -> bool:
    """The function checks if a specific character is within a specific string (parameters) it is true if the character is found and false if it isn't the while loop is to check each index of the search string if it matches it is true if not false and checks the next index."""
    assert len(char_searched) == 1
    index = 0
    while index < len(search_string):
        if search_string[index] == char_searched:
            return True
        index += 1
    return False


def emojified(guess: str, scrt_word: str) -> str:
    """Establishing a function "emojified" and checks the lengths of the guess and secret word to make sure they can be compared, while also establshing an index value and a place to store emojified if character is correct at correct index green, contains char for yellow, white for else."""
    assert len(guess) == len(scrt_word)
    emojified_str = ""
    index = 0
    
    while index < len(guess):
        guess_char = guess[index]
        scrt_char = scrt_word[index]
        
        if guess_char == scrt_char:
            emojified_str += GREEN_BOX
        elif contains_char(scrt_word, guess_char):
            emojified_str += YELLOW_BOX
        else:
            emojified_str += WHITE_BOX
        
        index += 1
    # returns the stored value and the += index ends the loop
    return emojified_str


def input_guess(expected_length: int) -> str: 
    """The function input guess has one perameter which is the expected length (length of the word that the user needs to guess) the function enters a loop until the user has a valid guess also establishes an f-string input which changes based on the length of the word."""
    while True:
        player_guess = input(f"Enter a {expected_length} character word: ")
        if len(player_guess) == expected_length:
            return player_guess
        else:
            print(f"That wasn't {expected_length} chars! Try again.")


def main() -> None:
    """The main function for the wordle game and establishes many of its systems like the wordle word, length of the wordle word, turns, and establishes a way to check for a correct guess."""
    wordle_word = "codes"
    expected_length = len(wordle_word)
    turns = 6
    correct_guess = False
    turn = 1

    print("Welcome to Wordle!")
    # while loop that displays the correct turn references previously established functions to represent the player guess and emoji results updates the turn amount and provides a check for a correct guess.
    while turn <= turns and not correct_guess:
        print(f"=== Turn {turn}/{turns} ===")
        player_guess = input_guess(expected_length)
        emoji_result = emojified(player_guess, wordle_word)
        print(emoji_result)

        if player_guess == wordle_word:
            correct_guess = True
        turn += 1
    # establishes the response to a correct and incorrect answer and uses f-strings to represent the turns
    if correct_guess:
        print(f"You won in {turn - 1}/{turns} turns!")
    else:
        print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
