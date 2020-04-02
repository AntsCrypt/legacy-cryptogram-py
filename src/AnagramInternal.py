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

    # get anagram setence
    def similar_setence(self, text):
        sentence = text.split(" ")
        for index in range(len(sentence)):
            words = self.similar_words(sentence[index])
            sentence[index] = random.choice(words)

        return " ".join(sentence)

    # Scan inputs to database
    def generator(self):
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

    # Print json database
    def dump(self):
        sys.stdout.write(json.dumps(generator))

    def load_database(self):
        sys.stdout.write("[!] loading...\n")
        with open(self.args["params"]["database"], 'rb') as json_data:
            self.database = json.loads(json_data.read())

    

    