from AnagramInternal import AnagramInternal
import sys

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
        self.print("[!] Similar words:", self.similar_words(text))

    def generator(self):
        self.print("[?] Write words:")
        self.load_generator()

        self.print("[!] Result database:", self.dump())
        

    def help(self):
        self.print("{}\n\t{}\t{}\n\t{}\n\n{}\n\t{}\n\t{}\n\t{}\n\t{}".format(
            "[!] params:",
            "-log"
            "-hash [number]",
            "-database [file]",
            "[!] commands:",
            "encode [text]",
            "decode [text]",
            "similar [word]",
            "generator"
        ))




