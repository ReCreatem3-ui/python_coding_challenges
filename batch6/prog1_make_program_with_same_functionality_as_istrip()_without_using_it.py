"""Removes the space characters from the beginning of a string, without using istrip()"""
def spacer():
    print("\n" * 20)

def remove_leading_spaces(s):
    result = ""
    leading_space = True
    for char in s:
        if char != ' ':
            leading_space = False
        if not leading_space:
            result += char
    return result

spacer()
input_string = input("Enter a string with leading spaces: ") 
output_string = remove_leading_spaces(input_string)
print(f"String without leading spaces: {output_string}") 