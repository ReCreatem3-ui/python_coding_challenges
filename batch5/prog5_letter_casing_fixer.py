"""Automatically fixes the casing of the inputed string, by changing the first letter to uppercase and the rest to lowercase"""

def spacer():
    for i in range(20):
        print("")

spacer()
name = input("Enter your name: ")
fixed_casing_name = name.title()
spacer()
print(f"Your name with fixed casing: {fixed_casing_name}")