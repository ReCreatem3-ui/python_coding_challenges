"""Identifies all the odd numbers in a given ten inputs and prints them"""
def spacer():
    for i in range (20):
        print("")

while True:
    try:
        spacer()
        odd_numbers = []
        count = 0
        for i in range(10):
            num = int(input(f"Enter number {count+1}: "))
            if num % 2 != 0:
                odd_numbers.append(num)
            count += 1
        
        print("=" * 40)
        print("The odd numbers you entered are:")
        print(", ".join(str(num) for num in odd_numbers))
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")
