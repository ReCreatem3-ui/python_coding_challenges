"""Calculates the sum of all ten numbers"""
def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        number_list = []
        for i in range(10):
            num = int(input(f"Enter number {i+1}: "))
            number_list.append(num)
        
        print("_" * 40)
        print(f"The sum of the numbers is {sum(number_list)}")
        break

    except ValueError:
        print("Invalid Input! Please enter numerical value")