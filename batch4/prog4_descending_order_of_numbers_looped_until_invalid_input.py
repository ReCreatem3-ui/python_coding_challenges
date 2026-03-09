"""Automatically sorts the inputted numbers in descending order repeatedly, until a non-numerical value is inputted."""

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
        
        reverse_sort = sorted(numbers, reverse=True)
        
        print("_" * 40)
        print("The numbers you entered in descending order are:")
        
        print(reverse_sort)
        
    except ValueError:
        spacer()
        print("Non-numerical value was inputted... Exiting program.")
        break