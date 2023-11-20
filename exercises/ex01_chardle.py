"""EX01 - Chardle - Step one of a series of steps to overthrow The New York Times (satire)."""

__author__ = "730529193"

five_word: str = input("Enter a 5-character word: ")
# if the word is unequal to 5 characters there is an error message
if len(five_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
# if the character guessed is unequal to 1 there is an error message
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
else: 
    print("Searching for " + single_character + " in " + five_word)
# code for instances
instance = 0

if five_word[0] == single_character:
    instance = instance + 1
    print(single_character + " found at index 0.")
    
if five_word[1] == single_character:
    instance = instance + 1
    print(single_character + " found at index 1.")
    
if five_word[2] == single_character:
    instance = instance + 1
    print(single_character + " found at index 2.")
    
if five_word[3] == single_character:
    instance = instance + 1
    print(single_character + " found at index 3.")
    
if five_word[4] == single_character:
    instance = instance + 1
    print(single_character + " found at index 4.")
    
if instance == 1:
    print(str(instance) + " instance of " + single_character + " found in " + five_word)
else:
    if instance > 1:
        print(str(instance) + " instances of " + single_character + " found in " + five_word)    

if instance == 0:
    print("No instances of " + single_character + " found in " + five_word)