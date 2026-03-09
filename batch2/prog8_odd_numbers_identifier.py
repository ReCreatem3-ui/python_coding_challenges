"""Prints all the odd numbers from 0 to 100"""
def spacer():
    for i in range (6):
        print("")

spacer()
print("The odd numbers from 0 to 100 are:")
for i in range(101):
    if i % 2 != 0:
        print(i, end=", ")
spacer()
