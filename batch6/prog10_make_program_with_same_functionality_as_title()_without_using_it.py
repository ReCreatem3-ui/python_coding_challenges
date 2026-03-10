"""Makes all the first letters of each word in a string uppercase without using the title() method"""

def spacer():
    for i in range(20):
        print("")

def manual_title(string):
    result = ""
    new_word = True 
    
    for char in string:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            result += char
            new_word = True
        elif new_word:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
            new_word = False
        else:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    return result

spacer()
input_string = input("Enter a string: ")
result = manual_title(input_string)
print(f"The string after applying manual_title is: '{result}'")