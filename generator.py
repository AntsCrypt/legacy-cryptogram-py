from collections import defaultdict
from slugify import slugify
import json
import sys
import re

# Creates instance of defaultdict
def tree(): 
    return defaultdict(tree)

# Add Word
def add(t, path):
    for node in path:
        t = t[node]

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

# Loads database
def run_generator():
    while True:
        # Scan word
        word = slugify(sys.stdin.readline())
        
        # Words over
        if len(word) == 0:
            break

        # Ignore multiple words in line
        if word.find('-') >= 0:
            continue

        # Count characters
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

        # Add Word
        add(generator, tree_key, word)

# Database
generator = tree()
        
# Runs command
if __name__ == '__main__':
    run_generator()
    sys.stdout.write(json.dumps(generator))
