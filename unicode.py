#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Dec 2019
# This is program word to unicode converter


def unicode_converter(word):
    # This takes a given word and converts it to the unicode equivalent

    unicode_word = ""

    letters = {
        "a": "61",
        "b": "62",
        "c": "63",
        "d": "64",
        "e": "65",
        "f": "66",
        "g": "67",
        "h": "68",
        "i": "69",
        "j": "6a",
        "k": "6b",
        "l": "6c",
        "m": "6d",
        "n": "6e",
        "o": "6f",
        "p": "70",
        "q": "71",
        "r": "72",
        "s": "73",
        "t": "74",
        "u": "75",
        "v": "76",
        "w": "77",
        "x": "78",
        "y": "79",
        "z": "7a",
    }

    # process
    for letter in word:
        if letter in letters:
            unicode_word = unicode_word + letters[letter] + " "
        else:
            return "This character is not in my list."

    return "In hexadecimal the word is " + unicode_word


def main():
    # This takes the user's word and passes it to UnicodeConverter()

    # input
    word = input("Type your word: ")

    # process
    word = unicode_converter(word)

    print(word)


if __name__ == "__main__":
    main()
