"""Prints Equal when the two numbers were equal"""

def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        if num1 == num2:
            spacer()
            print("Equal")
        else:
            spacer()
        break
    except ValueError:
        print("Invalid Input! Your OS has been comprimized")