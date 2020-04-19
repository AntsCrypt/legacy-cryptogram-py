from AnagramInternal import AnagramInternal
import sys

help_str = """[!] params:
\t-log
\t-hash [password]
\t-jumps [pass]
\t-limit [max]
\t-database [file]
[!] commands:
\tencode [text]
\tdecode [text]
\tsimilar [word]
\tgenerator
\n"""

class AnagramCommand(AnagramInternal):
    def encode(self, text):
        self.load_database()
        text = self.similar_sentence(text)
        self.print("[!] Encoded text:", text)

    def decode(self, text):
        self.load_database()
        text = self.similar_sentence(text, inverse = True)
        self.print("[!] Decoded text:", text)

    def similar(self, text):
        self.load_database()

        # Similar sentences
        if " " in text:
            self.print("[!] Similar sentences:", self.similar_sentences(text))

        # Similar words
        else:
            self.print("[!] Similar words:", self.similar_words(text))

    def generator(self):
        self.print("[?] Write words:")
        self.load_generator()

        self.print("[!] Result database:", self.dump())
        

    def help(self):
        sys.stderr.write(help_str)




