"""Manually convert a string to Uppercase without using the built-in upper() method"""

def spacer():
    for i in range(20):
        print("")

def manual_uppercase(string):
    uppercase_string = []
    for char in string:
        if not 'A' <= char <= 'Z':
            uppercase_string.append(chr(ord(char) - 32))
        else:
            uppercase_string.append(char)
    return ''.join(uppercase_string)

spacer()
input_string = input("Enter a string: ")
lowercase_result = manual_uppercase(input_string)
print(f"String in uppercase: {lowercase_result}")