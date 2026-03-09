"""Removes excessive spaces from a string."""

def spacer():
    for i in range(2):
        print("")

def remove_excessive_spaces(s):
    return ' '.join(s.split())

spacer()
name = input("Enter your name with excessive spaces: ")
result = remove_excessive_spaces(name)
print(f"Your name with excessive spaces removed: {result}")