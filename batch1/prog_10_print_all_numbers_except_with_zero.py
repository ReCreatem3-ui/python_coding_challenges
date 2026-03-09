"""Prints all the numbers from 0-100 except those with zero in them"""
def spacer():
    for i in range (20):
        print("")

spacer()
print("The numbers from 1 to 100 that do not contain the digit '0' are:")
for i in range(101):
    if i % 10 != 0:
        print(i, end=", " if i < 100 else "\n") 