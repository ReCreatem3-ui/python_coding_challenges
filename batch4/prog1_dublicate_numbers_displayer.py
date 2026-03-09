"""Displays all the duplicate numbers within the ten numbers repeatly, until a non-numerical value is inputted."""

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
        
        duplicates = set() 
        seen = set() 
        
        for num in numbers:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        if duplicates:
            print("_" * 40)
            print("The duplicate numbers you entered are:")
            print(duplicates)
        else:
            print("_" * 40)
            print("No duplicate numbers were found.")
    except ValueError:
        print("Non-numerical value was inputted... Exiting program.")
        break

