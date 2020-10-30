"""
Given a string of words, reverse all the words

start = "This is the best"
finish = "best the is This"
"""

# Method 1 using builtin split, keeping the structure of the words intact
def reverse_str(string):
    return print(" ".join(reversed(string.split())))

reverse_str("This is the best")

# Method 2 not using python built in, reversing the string and the words
def reverse_v2(string):
    
    length = len(string)
    spaces = [" "]
    words = []
    i = 0

    while i < length:
        if string[i] not in spaces:
            word_start = i

            while i < length and string[i] not in spaces:
                i += 1
                
            words.append(string[word_start:i])
        
        i += 1

    return print("".join(reversed(string)))


reverse_v2("This is the best")

