"""Changes the casing of the inputed string to lowercase"""

def spacer():
    for i in range(20):
        print("")

spacer()
name = input("Enter your name: ")
lowercase_name = name.lower()
spacer()
print(f"Your name in uppercase: {lowercase_name}")