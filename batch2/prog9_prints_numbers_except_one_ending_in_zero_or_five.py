"""Prints only the numbers from 0 to 100 that do not end in 0 or 5"""

def spacer():
    for i in range (6):
        print("")

spacer()
print("The numbers from 0 to 100 that do not end in 0 or 5 are:")
for i in range(101):
    if i % 10 != 0 and i % 10 !=5:
        print(i, end=", ")
spacer()