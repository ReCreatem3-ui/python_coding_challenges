"""Checks if the string starts with a specific substring without using the startswith() method"""

def spacer():
    for i in range(20):
        print("")

def manual_startswith(string, substring):
    if len(substring) > len(string):
        return False
    return string[:len(substring)] == substring

spacer()
input_string = input("Enter a string: ")
substring = input("Enter the substring to check: ")
if manual_startswith(input_string, substring):
    print(f"The string starts with '{substring}'")
else:
    print(f"The string does not starts with '{substring}'")