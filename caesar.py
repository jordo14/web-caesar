def encrypt(text, rot):
    encrypted = ""
    for letter in text:
        newcharacter = rotate_character(letter, rot)
        if letter.isupper():
            newcharacter = newcharacter.upper()
        encrypted += newcharacter
        
    return encrypted

import string
alphabet = list(string.ascii_lowercase)

def alphabet_position(letter):  #returns the index value of character in alphabet
    letter = letter.lower()
    return alphabet.index(letter)
  

def rotate_character(char, rot):
    newstring = ""
    if char.isalpha():
        charinstr = int(alphabet_position(char)) + rot  #returns non-alphebetical characters and spaces
    else:
        return char

    if charinstr < 26:                              
        newstring = alphabet[charinstr]                 #rotates character
    else:
        newstring = alphabet[charinstr % 26]

    return newstring
