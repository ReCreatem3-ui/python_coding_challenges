"""Automatically reverses the casing of the inputed string, by changing uppercase letters to lowercase and lowercase letters to uppercase"""

def spacer():
    for i in range(20):
        print("")

spacer()
name = input("Enter your name: ")
reversed_casing_name = name.swapcase()
print(f"Your name with reversed casing: {reversed_casing_name}")