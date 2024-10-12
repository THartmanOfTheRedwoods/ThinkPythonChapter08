#!/usr/bin/env python3

"""
See if you can write a function that does the same thing as the shell command
!head. It should take as arguments the name of a file to read, the number of lines
to read, and the name of the file to write the lines into. If the third parameter
is None, it should display the lines rather than write them to a file.
"""
def head(in_file, num_lines, out_file=None):
    lines = []
    with open(in_file, 'r') as file:
        for _ in range(num_lines):
            lines.append(file.readline())
    if out_file:
        with open(out_file, 'w') as file:
            file.writelines(''.join(lines))
    else:
        print(''.join(lines))

head('files/dracula.txt', 3, 'files/output.txt')
head('files/dracula.txt', 3)

