from collections import defaultdict
import sys, random, re

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


# Scan text from args
def scan_text(ignore):
    words = sys.argv[ignore:len(sys.argv)]
    return " ".join(words)

# get word same letters
def similar_words(database, word):
    enter = database
    for go in word_tree(word):
        enter = enter[go]

    return enter


def randomize_setence(database, text):
    sentence = text.split(" ")
    for index in range(len(sentence)):
        words = similar_words(database, sentence[index])
        sentence[index] = random.choice(words)

    return " ".join(sentence)
