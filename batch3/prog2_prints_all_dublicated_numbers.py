"""Prints all the numbers with duplicates within 10 numbers inputed by the user; displays the first entry of each duplicate number only"""

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
        spacer()
        print("The dublicate numbers you entered are:")
        duplicates = set()
        for num in numbers:
            if numbers.count(num) > 1:
                duplicates.add(num)
        for num in duplicates:
            print(num, end=", ")
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")