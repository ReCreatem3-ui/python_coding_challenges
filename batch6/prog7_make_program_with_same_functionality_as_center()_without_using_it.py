"""Adds a space to the beginning and the end of a string to print it on the center, without using the center() method"""

def spacer():
    for i in range(20):
        print("")

def manual_center(string, width):
    if len(string) >= width:
        return string
    total_padding = width - len(string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    return " " * left_padding + string + " " * right_padding

spacer()
input_string = input("Enter a string: ")
width = int(input("Enter the destined width: "))
result = manual_center(input_string, width)
print(f"The string after applying manual_ljust is: '{result}'") 