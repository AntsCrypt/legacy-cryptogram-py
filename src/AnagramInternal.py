from slugify import slugify
from functions import *
import random, json, sys, re

class AnagramInternal:
    database = tree()
    args = {
        "cmd":"",
        "text":"",
        "params": {
            "database":"database.json",
            "hash": "2345678"
        }
    }

    # Load arguments
    def __init__(self):
        index = 1
        while index < len(sys.argv):
            # Load params
            if sys.argv[index][0] == "-":
                self.args["params"][sys.argv[index][1:]] = sys.argv[index + 1]
                index += 1
            
            # Load command
            elif self.args["cmd"] == "" and not sys.argv[index].count("anagram"):
                self.args["cmd"] = sys.argv[index]

            # Load text
            elif self.args["cmd"] != "":
                self.args["text"] = " ".join(sys.argv[index:])
                break

            index += 1

        #set random control
        random.seed(self.args["params"]["hash"])

    # get word same letters
    def similar_words(self, word):
        # search words
        try:
            enter = self.database
            for go in word_tree(word):
                enter = enter[go]
        # word not exist in database
        except KeyError:
            return [word]
        
        # similar words exist in database
        else:
            return enter

    # get anagram sentence
    def similar_sentence(self, text, inverse = False):
        # separe text
        sentence = self.randomize_sentence(text.split(" "), inverse = inverse)

        # anagram words
        for index in range(len(sentence)):            
            sentence[index] = self.randomize_word(sentence[index], inverse = inverse)

        # anagram sentence
        return " ".join(sentence)

    def randomize_word(self, word, inverse = False):
        # other words
        words = self.similar_words(word)
        len_words = len(words)

        # search word
        try:
            pos = words.index(word)

        # word not found
        except ValueError:
            return word

        # random word
        rand = random.randrange(0, len_words)

        # decode
        if inverse:
            pos -= rand

        # encode
        elif (pos + rand) >= len_words:
            pos += rand - len_words
        
        # encode
        else:
            pos += rand

        return words[pos]

    def randomize_sentence(self, array_text, inverse = False):
        return array_text

    # Print json database
    def dump(self):
        sys.stdout.write(json.dumps(self.database))

    # Scan inputs to database
    def load_generator(self):
        while True:
            # Scan word
            word = slugify(sys.stdin.readline())
            
            # Words over
            if len(word) == 0:
                break

            # Ignore multiple words in line
            if word.find('-') >= 0:
                continue

            # Add Word
            add(self.database, word_tree(word), word)

    def load_database(self):
        sys.stdout.write("[!] loading...\n")
        with open(self.args["params"]["database"], 'rb') as json_data:
            self.database = json.loads(json_data.read())

    

    