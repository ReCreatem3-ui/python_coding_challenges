"""Determines if the ten numbers inputed by the user were Unique or Duplicaton; program was kept on loop, until a non-numerical value is entered."""

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
        
        if len(numbers) == len(set(numbers)):
            print("_" * 10)
            print("Status: Unique")
        else:
            print("_" * 40)
            print("Status: Duplicate")
            
    except ValueError:
        spacer()
        print("Non-numerical value was inputed...Exiting program.")
        break