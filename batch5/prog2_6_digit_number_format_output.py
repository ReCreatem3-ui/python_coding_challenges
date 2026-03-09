"""Automatically converts the inputed number into a 6 digit number, by adding zeros at the beginning"""

def spacer():
    for i in range(20):
        print("")   

spacer()
number = int(input("Enter a number: "))
formatted_number = f"{number:06d}"
print(f"The number you entered, formatted as a 6 digit number: {formatted_number}")