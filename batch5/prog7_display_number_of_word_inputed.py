"""Counts the number of words in the inputed string and displays it"""

def spacer():
    for i in range(20):
        print("")

spacer()
text = input("Enter a sentence: ")
word_count = len(text.split())
print(f"The number of words in the sentence is: {word_count}")