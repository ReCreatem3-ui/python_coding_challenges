"""Returns the first location of a substring in a string, without using the built-in index() function"""

def spacer():
    for i in range(20):
        print("")

def find_substring(string, substring):
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    raise ValueError("Substring not found")

spacer()
input_string = input("Enter a string: ")
substring = input("Enter the substring to find: ")
try:
    result = find_substring(input_string, substring)
    print(f"The substring '{substring}' is found at index {result}.")
except ValueError as e:
    print(e)