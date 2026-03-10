"""Adds zero characters to the left of a string until it reaches a specified length, without using the built-in zfill() method."""

def spacer():
    for i in range(20):
        print("")

def custom_zfill(string, width):
    if len(string) >= width:
        return string
    return "0" * (width - len(string)) + string

spacer()
input_string = input("Enter a string: ")
width = int(input("Enter the destined width: "))
result = custom_zfill(input_string, width)
print(f"The string after applying custom_zfill: '{result}'")
