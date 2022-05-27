# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# A question: How can someone use a while loop for this same program?

def find_anagram(word, anagram):
    # [assignment] Add your code here
    first_word = list(word)
    second_word =list(anagram)
    word_check = []

    for letter in first_word:
        if letter in second_word:
            word_check.append(letter)

    if (len(first_word) == len(word_check)):
        print("True")
    else:
        print("False")
    

find_anagram("hello", "check")
