from slugify import slugify
from common import *
import json
import sys

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

        # Add Word
        add(generator, word_tree(word), word)

# Database
generator = tree()
        
# Runs command
if __name__ == '__main__':
    run_generator()
    sys.stdout.write(json.dumps(generator))
