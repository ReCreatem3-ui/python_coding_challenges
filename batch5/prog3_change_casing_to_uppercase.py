"""Changes the casing of the inputed string to uppercase"""

def spacer():
    for i in range(20):
        print("")

spacer()
name = input("Enter your name: ")
uppercase_name = name.upper()
spacer()
print(f"Your name in uppercase: {uppercase_name}")