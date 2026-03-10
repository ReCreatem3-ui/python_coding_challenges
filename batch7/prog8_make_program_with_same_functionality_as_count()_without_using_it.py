"""Counts how many times the requested letter appears in a string without using the count() method"""

def spacer():
    for i in range(20):
        print("")

def count_letter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

spacer()
input_string = input("Enter a string: ")
letter = input("Enter the letter to count: ")
result = count_letter(input_string, letter)
print(f"The letter '{letter}' appears {result} times in the string.")