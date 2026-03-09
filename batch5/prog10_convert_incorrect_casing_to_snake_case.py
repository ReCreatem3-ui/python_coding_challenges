"""Changes the incorrect casing into snake case"""

def spacing():
    for i in range(20):
        print("")

spacing()
name = input("Enter your name: ")
snake_case_name = name.lower().replace(" ", "_")
print(f"Your name in snake case: {snake_case_name}")