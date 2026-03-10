"""Checks if all the characters in a string are uppercase without using the isupper() method"""

def spacer():
    for i in range(20):
        print("")

def manual_isupper(string):
    has_alpha = False
    for char in string:
        if 'a' <= char <= 'z':
            return False
        if 'A' <= char <= 'Z':
            has_alpha = True
    return has_alpha

spacer()
input_string = input("Enter a string: ")
if manual_isupper(input_string):
    print('All characters are uppercase.')
else:
    print('Not all characters are uppercase.')