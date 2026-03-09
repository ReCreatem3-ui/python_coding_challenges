"""Calculates the exponent of the two numbers"""

def spacer():
    for i in range (2): 
        print("")

while True:
    try:
        spacer()
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        set_number_limit = 100
        if abs(num1) > set_number_limit or abs(num2) > set_number_limit:
            raise OverflowError
        
        number_sum = num1 ** num2
        
        spacer()
        print(f"The exponent of {num1} and {num2} is {number_sum}") 
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")
    except OverflowError:
        print("The Value is too large to compute! Please enter smaller numbers.")