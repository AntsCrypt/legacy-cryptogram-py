from slugify import slugify
from functions import *
import itertools, random, json, sys, re

class AnagramInternal:
    database = tree()
    args = {
        "cmd": "",
        "text": "",
        "params": {
            "database": "database.json",
            "hash": "2345678",
            "log": ""
        }
    }

    # Load arguments
    def __init__(self):
        index = 1
        while index < len(sys.argv):
            # Load params
            if sys.argv[index][0] == "-":
                self.args["params"][sys.argv[index][1:]] = sys.argv[index + 1]
                if sys.argv[index][1:] != "log":
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
        self.random_reset()

    # get all similar words same letters
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

    # get all similar sentences
    def similar_sentences(self, text):
        sentence = text.split(" ")
        len_sentence = len(sentence)
        sentences = []

        # create all possibilities
        for index in range(len_sentence):
            sentence[index] = self.similar_words(sentence[index])

        # mount anagrams
        for possible_sentences in list(itertools.permutations(sentence)):
            for possibles_words in list(itertools.product(*possible_sentences)):
                sys.stdout.write(" ".join(possibles_words) + "\n")

        return ""

    # get anagram sentence
    def similar_sentence(self, text, inverse = False):
        # separe text
        sentence = text.split(" ")
        
        # setence decode
        if not inverse:
            sentence = self.randomize_sentence(sentence, inverse = False)

        # anagram words
        self.random_reset()
        for index in range(len(sentence)):            
            sentence[index] = self.randomize_word(sentence[index], inverse = inverse)

        # sentence encode
        if inverse:
            sentence = self.randomize_sentence(sentence, inverse = True)

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
        # reboot random
        self.random_reset()

        len_sentence = len(array_text)
        randons = self.random_array(len_sentence)
        sentence = []

        # Suffle setence
        for index in randons:
            sentence.append(array_text[index])

        if not inverse:
            return sentence

        # Resuffle sentence
        for index in range(len_sentence):
            sentence[randons[index]] = array_text[index]

        return sentence

    # Generate array with random numbers
    def random_array(self, size):
        arr = []
        for index in range(size):
            while True:
                rand = random.randrange(0, size)
                if not rand in arr:
                    arr.append(rand)
                    break
        return arr

    
    # Reload Hash token
    def random_reset(self):
        random.seed(self.args["params"]["hash"])

    # Print json database
    def dump(self):
        human = len(self.args["params"]["log"]) > 0
        return json.dumps(self.database, indent=human)

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
        self.print("[!] loading...\n")
        with open(self.args["params"]["database"], 'rb') as json_data:
            self.database = json.loads(json_data.read())

    # Print with optional strings verify
    def print(self, optional, text_array = ""):

        # concatenate text with breakline
        if isinstance(text_array, list):
            text_string = "\n".join(text_array)
        
        # normal text
        else:
            text_string = text_array

        # verify show
        show_optional = len(self.args["params"]["log"]) and len(optional)
        show_string = len(text_string)

        # show logs
        if show_optional:
            sys.stdout.write(optional)

        # prints space
        if show_optional and show_string:
            sys.stdout.write("\n")

        # show output
        if show_string:
           sys.stdout.write(text_string) 

        # prints EOS
        if show_optional:
            sys.stdout.write("\n")