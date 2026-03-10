"""Checks if all the characters in a string are lowercase without using the islower() method"""

def spacer():
    for i in range(20):
        print("")

def manual_islower(string):
    has_alpha = False
    for char in string:
        if 'A' <= char <= 'Z':
            return False
        if 'a' <= char <= 'z':
            has_alpha = True
    return has_alpha

spacer()
input_string = input("Enter a string: ")
if manual_islower(input_string):
    print('All characters are lowercase.')
else:
    print('Not all characters are lowercase.')