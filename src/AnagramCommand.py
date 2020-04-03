from AnagramInternal import AnagramInternal
import sys

class AnagramCommand(AnagramInternal):
    def encode(self, text):
        self.load_database()
        text = self.similar_setence(text)
        sys.stdout.write("[!] Encoded text: {}".format(text))

    def decode(self, text):
        self.load_database()
        text = self.similar_setence(text, inverse = -1)
        sys.stdout.write("[!] Decoded text: {}".format(text))

    def similar(self, text):
        self.load_database()
        sys.stdout.write("[!] Similar words: {}".format(", ".join(self.similar_words(text))))

    def generator(self):
        self.load_generator()
        self.dump()

    def help(self):
        sys.stdout.write("{}\n\t{}\n\t{}\n\n{}\n\t{}\n\t{}\n\t{}\n\t{}".format(
            "[!] params:",
            "-hash [number]",
            "-database [file]",
            "[!] commands:",
            "encode [text]",
            "decode [text]",
            "similar [word]",
            "generator"
        ))




