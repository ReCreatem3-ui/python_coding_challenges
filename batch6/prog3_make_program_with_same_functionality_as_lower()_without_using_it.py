"""Manually convert a string to lowercase without using the built-in lower() method"""
def spacer():
    for i in range(20):
        print("")

def manual_lowercase(string):
    lowercase_string = []
    for char in string:
        if 'A' <= char <= 'Z':
            lowercase_string.append(chr(ord(char) + 32))
        else:
            lowercase_string.append(char)
    return ''.join(lowercase_string)

spacer()
input_string = input("Enter a string: ")
lowercase_result = manual_lowercase(input_string)
print(f"String in lowercase: {lowercase_result}")