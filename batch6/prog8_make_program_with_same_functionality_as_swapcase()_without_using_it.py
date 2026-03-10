"""Reverses the case of each character in a string without using the built-in swapcase() method"""

def spacer():
    for i in range(20):
        print("")

def manual_swapcase(string):
    for char in string:
        if 'a' <= char <= 'z':
            yield chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            yield chr(ord(char) + 32)
        else:
            yield char

spacer()
input_string = input("Enter a string: ")
result = ''.join(manual_swapcase(input_string))
print(f"String with swapped casing: '{result}'")