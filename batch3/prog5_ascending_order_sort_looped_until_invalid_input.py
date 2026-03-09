"""Automatically sorts the inputted numbers in ascending order repeatedly, until a non-numerical value is inputted."""

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
        
        sorted_numbers = sorted(numbers)
        
        print("_" * 40)
        print("The numbers you entered in ascending order are:")
        
        print(sorted_numbers)
        
    except ValueError:
        spacer()
        print("Non-numerical value was inputted... Exiting program.")
        break