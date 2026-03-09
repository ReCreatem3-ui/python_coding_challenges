"""Prints all numbers from 1-100 that was even"""
def spacer():
    for i in range (20):
        print("")

spacer()
even_numbers = []
for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("The even numbers from 1 to 100 are:")
print(", ".join(str(num) for num in even_numbers))
