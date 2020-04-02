from AnagramInternal import AnagramInternal
import sys

class AnagramCommand(AnagramInternal):
    def encode(self, text):
        text = self.similar_setence(text)
        sys.stdout.write("[!] Encoded text: {}".format(text))

    def decode(self, text):
        pass

    def similar(self, text):
        print("[!] Similar words:", ", ".join(self.similar_words(text)))