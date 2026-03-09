"""Prints all numbers without duplicates within 10 numbers inputed by the user"""

def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        numbers = []
        for i in range(10):
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            unique_numbers = set(numbers)
        spacer()
        print("The unique numbers you entered are:")
        for num in unique_numbers:
            print(num, end=", ")
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")