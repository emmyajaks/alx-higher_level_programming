#!/usr/bin/python3
output = ''
for char in range(ord('a'), ord('z') + 1):
    if char != ord('q') and char != ord('e'):
        output += chr(char)

print(output, end='')
