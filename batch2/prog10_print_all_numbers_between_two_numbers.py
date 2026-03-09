"""Prints all the numbers between two numbers inputed by the user"""

def spacer():
    for i in range (2):
        print("")

while True:
    try:
        spacer()
        num1 = int(input("Enter the first number: "))
        num2 = (int(input("Enter the second number: ")))

        if num1 < num2:
            spacer()
            print(f"The numbers between {num1} and {num2} are:")
            for i in range(num1 + 1, num2):
                print(i, end=", ")
        elif num1 > num2:
            spacer()
            print(f"The numbers between {num2} and {num1} are:")
            for i in range(num2 + 1, num1):
                print(i, end=", ")
        else:
            spacer()
            print("Both numbers are the same. Please enter different numbers.")
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")
