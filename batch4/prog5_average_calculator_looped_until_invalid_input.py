"""Calculates the average of a series of numbers entered by the user, until an invalid input is given."""

def spacer():
    for i in range(5):
        print("")

while True:
    try:
        numbers = []
        spacer()
        for i in range(10):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        
        average = sum(numbers) / len(numbers)
        
        print("_" * 40)
        print(f"The average of the numbers you entered is: {average}")
        
    except ValueError:
        spacer()
        print("Non-numerical value was inputted... Exiting program.")
        break