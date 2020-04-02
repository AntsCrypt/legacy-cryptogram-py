from common import *
import json
import sys

database = tree()

def encode(text):
   text = randomize_setence(database, text)
   sys.stdout.write("[!] Encoded text: {}".format(text))

    


def decode(text):
    pass

def similar(text):
    print("[!] Similar words:", ", ".join(similar_words(database, text)))


# run command
if __name__ == '__main__':
    
    # wait
    sys.stdout.write("[!] loading...\n")
    
    # load database
    with open('output.json', 'rb') as json_data:
        database = json.loads(json_data.read())

    # select command
    try:
        if sys.argv[1] == "encode":
            encode(scan_text(3))
        
        elif sys.argv[1] == "decode":
            encode(scan_text(3))

        elif sys.argv[1] == "similar":
            similar(scan_text(2))
    
    except (IndexError, KeyError):
        sys.stdout.write("[!] ERROR! use: anagram [encode/decode] [hash] [text]")

    finally:
        print()

