"""Prints Not Equal when the two numbers were not equal"""

def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        if num1 != num2:
            spacer()
            print("Not Equal")
        else:
            spacer()
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")