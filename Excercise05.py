#!/usr/bin/env python3

import re

def check_pale(sentence):
   pattern = r'.*(pale\w*|pallor).*'
   return True if re.match(pattern, sentence) else False

def main():
    with open('files/TheCountofMnteCristo.txt', 'r') as file:
        count = 0
        for line in file:
            if check_pale(line.strip()):
                print(line)
                count += 1

    print(f"Lines with some form of pale: {count}")

if __name__ == '__main__':
    main()