"""EX01 - Chardle - First step in toppling The New York Times (satire)."""

__author__ = "730529193"

five_word: str = input("Enter a 5-character word: ")
# if the word is unequal to 5 characters there is an error message
if len(five_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    print(five_word)
# if the character guessed is unequal to 1 there is an error message
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
else: 
    print(single_character)
    print("Searching for " + single_character + " in " + five_word)
# code for instances and matching indices
instance = 0
matching = False
if five_word[0] == single_character:
    instance = instance + 1
    print(single_character + " found at index 0. ")
    matching = False
if five_word[1] == single_character:
    instance = instance + 1
    print(single_character + " found at index 1. ")
    matching = True
if five_word[2] == single_character:
    instance = instance + 1
    print(single_character + " found at index 2. ")
    matching = True
if five_word[3] == single_character:
    instance = instance + 1
    print(single_character + " found at index 3. ")
    matching = True
if five_word[4] == single_character:
    instance = instance + 1
    print(single_character + " found at index 4. ")
    matching = True
if instance == 1:
    print(str(instance) + " instance of " + single_character + " found in " + five_word)
else:
    if instance > 1:
        print(str(instance) + " instances of " + single_character + " found in " + five_word)    
if matching is not True:
    print("No instances of " + single_character + " found in " + five_word)