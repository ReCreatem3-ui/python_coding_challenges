"""Displays the number with the largest value repeatly, until a non-numerical value was inputed"""

def spacer():
    for i in range(5):
        print("")

while True:
    try:
        spacer()
        numbers = []
        for i in range(10):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
        
        largest_number = max(numbers)
        print("_" * 40)
        print(f"The largest number you entered is: {largest_number}")
    except ValueError:
        spacer()
        print("Non-numerical value was inputed...Exiting program.")
        break
