"""Returns the first location of the last character in a string starting from the last character, without using the built-in rindex() function"""

def spacer():
    for i in range(20):
        print("")

def manual_rindex(string, character):
    for i in range(len(string) - 1, -1, -1):
        if string[i] == character:
            return i
    raise ValueError("Character not found")

spacer()
input_string = input("Enter a string: ")
character = input("Enter the character to find: ")
try:
    result = manual_rindex(input_string, character)
    print(f"The character '{character}' is found at index {result}.")
except ValueError as e:
    print(e)