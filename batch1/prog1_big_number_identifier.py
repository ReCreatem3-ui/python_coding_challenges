"""Indentifies the number with higher value"""
def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        if num1 > num2:
            spacer()
            print(f"{num1} is bigger than {num2}")
        else:
            spacer()
            print(f"{num2} is bigger than {num1}")
        break
    except ValueError:
        print("Invalid Input! Your OS has been comprimized")