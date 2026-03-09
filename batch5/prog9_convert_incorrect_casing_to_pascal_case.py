"""Changes the incorrect casing into pascal case"""

def spacing():
    for i in range(20):
        print("")

spacing()
name = input("Enter your name: ")
pascal_case_name = name.title().replace(" ", "")
print(f"Your name in pascal case: {pascal_case_name}")