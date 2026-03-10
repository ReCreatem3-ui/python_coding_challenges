"""Removes the excessive space characters from the end of a string, without using rstrip()"""
def spacer():
    print("\n" * 20)

def remove_trailing_spaces(s):
    result = ""
    trailing_space = True
    for char in reversed(s):
        if char != ' ':
            trailing_space = False
        if not trailing_space:
            result = char + result
    return result

spacer()
input_string = input("Enter a string with trailing spaces: ")
output_string = remove_trailing_spaces(input_string)
print(f"String without trailing spaces: '{output_string}'")