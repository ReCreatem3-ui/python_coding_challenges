"""Calculates the quotient between the two numbers"""

def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        
        number_sum = num1 / num2
        
        spacer()
        print(f"The quotient of {num1} and {num2} is {number_sum}")
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")