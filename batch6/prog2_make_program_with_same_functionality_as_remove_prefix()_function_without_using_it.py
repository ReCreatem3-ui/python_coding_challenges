"""Removes the character at the beginning of a string if it matches the specified character, without using the built-in remove_prefix() function"""
def spacer():
    for i in range(20):
        print("")

def manual_remove_prefix(s, prefix):
    if len(s) >= len(prefix) and s[:len(prefix)] == prefix:
        return s[len(prefix):]
    return s

spacer()
input_string = input("Enter a string: ") 
prefix_to_remove = input("Enter the prefix to remove: ")
result_string = manual_remove_prefix(input_string, prefix_to_remove)
print(f"String after removing prefix: {result_string}") 