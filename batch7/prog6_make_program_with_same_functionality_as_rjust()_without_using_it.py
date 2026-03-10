"""Adds a space to the start of a string until it reaches a specified length, without using the rjust() method"""

def spacer():
    for i in range(20):
        print("")

def manual_rjust(string, width):
    if len(string) >= width:
        return string
    return " " * (width - len(string)) + string

spacer()
input_string = input("Enter a string: ")
width = int(input("Enter the destined width: "))
result = manual_rjust(input_string, width)
print(f"The string after applying manual_rjust is: '{result}'") 