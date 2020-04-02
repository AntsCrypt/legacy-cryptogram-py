from collections import defaultdict
import sys, re

# Creates instance of defaultdict
def tree(): 
    return defaultdict(tree)

# Add value to tree
def add(t, patch, value):
    i = 0
    for node in patch:
        i += 1
        if i == len(patch): 
            if not isinstance(t[node], list):
                t[node] = [value]
            elif not value in t[node]:
                t[node].append(value)
        t = t[node]

# Count number of vowels
def vowels(string):
    return len(re.sub('[^aeiou]', '', string))

def word_tree(word):
    count_char = {}
    len_char = []
    for char in word:
        count_char[char] = word.count(char)

    # Key char
    for char in count_char.keys():
        len_char.append(char  + str(count_char[char]))
    
    # Key count
    len_vowel = str(vowels(word))
    len_word = str(len(word))
    
    # All keys
    tree_key = [len_word, len_vowel]
    tree_key.extend(sorted(len_char))

    return tree_key