"""Checks if the string ends with a specific substring without using the endswith() method"""

def spacer():
    for i in range(20):
        print("")

def manual_endswith(string, substring):
    if len(substring) > len(string):
        return False
    return string[-len(substring):] == substring

spacer()
input_string = input("Enter a string: ")
substring = input("Enter the substring to check: ")
if manual_endswith(input_string, substring):
    print(f"The string ends with '{substring}'")
else:
    print(f"The string does not end with '{substring}'")