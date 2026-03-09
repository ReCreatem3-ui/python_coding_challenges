"""Counts all the even numbers within 10 numbers """

while True:
    try:
        even_numbers = []
        for i in range(10):
            num = int(input(f"Enter number {i+1}: "))
            if num % 2 == 0:
                even_numbers.append(num)
        print("_" * 40)
        print(f"The even numbers you entered are: {even_numbers}")
        print(f"The total count of even numbers you entered is: {len(even_numbers)}")
        break
    except ValueError:
        print("Invalid Input! Please enter numerical value")