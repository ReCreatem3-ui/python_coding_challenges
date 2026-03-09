"""Calculates the difference of all the numbers from 1 to 10"""
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
        difference = number_list[0] 
        for num in number_list[1:]:
            difference -= num
        print(f"The difference of the numbers is {difference}")
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")
