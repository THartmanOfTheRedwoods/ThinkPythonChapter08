#!/usr/bin/env python3

import re


def check_word(five_letter_word):
    five_letter_word = five_letter_word.upper()
    if 'E' not in five_letter_word:
        return False
    # Matches any world that has an E at the 3rd or 5th character or contains any of the letters SPADCLRK
    # \b is a word boundary, \w matches any character, ?: is a non-capturing group, {N} represents the
    # number of times a pattern occurs.
    pattern = r'\b(?:\w{2}E\w+|\w{4}E\w*|\w*[SPADCLRK]\w*)\b'
    return False if re.match(pattern, five_letter_word, re.IGNORECASE) else True

def run():
    print( check_word( 'BELLE' ) )
    print( check_word( 'JIVES' ) )
    print( check_word( 'HELLO' ) )
    print( check_word( 'ENJOY' ) )

def main():
    count = 0
    with open( 'files/words.txt', 'r' ) as file:
        for word in file:
            word = word.strip()
            if len( word ) == 5 and check_word( word ):
                print( word )
                count += 1

    print( f"A total of {count} words could still match." )


if __name__ == '__main__':
    main()