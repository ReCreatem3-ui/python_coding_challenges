"""Adds a space to the end of a string until it reaches a specified length, without using the ljust() method"""

def spacer():
    for i in range(20):
        print("")

def manual_ljust(string, width):
    if len(string) >= width:
        return string
    return string + " " * (width - len(string))

spacer()
input_string = input("Enter a string: ")
width = int(input("Enter the destined width: "))
result = manual_ljust(input_string, width)
print(f"The string after applying manual_ljust is: '{result}'") 