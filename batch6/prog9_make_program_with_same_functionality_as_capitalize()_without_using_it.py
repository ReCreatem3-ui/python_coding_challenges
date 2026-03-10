"""Capitalizes the first letter of a string without using the built-in capitalize() method"""

def spacer():
    for i in range(20):
        print("")

def manual_capitalize(string):
    if not string:
        return string
    first_char = string[0]
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
    return first_char + string[1:]

spacer()
input_string = input("Enter a string: ")
result = manual_capitalize(input_string)
print(f"The string after applying manual_capitalize: '{result}'")