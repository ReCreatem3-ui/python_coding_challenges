"""Dislpay the number with the most duplicates in a list of numbers. Loop until invalid input is given."""

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
        
        counts = {}
        for num in numbers:
            counts[num] = counts.get(num, 0) + 1
        
        most_frequent = max(counts, key=counts.get)
        highest_count = counts[most_frequent]
        
        print("_" * 40)
        
        if highest_count > 1:
            print(f"The number with the most duplicates is: {most_frequent}")
            print(f"It appeared {highest_count} times.")
        else:
            print("No duplicate numbers were found.")

    except ValueError:
        spacer()
        print("\nNon-numerical value was inputted... Exiting program.")
        break