from slugify import slugify
import json
import re

generator = {}

def vogais(string):
    return len(re.sub('[^aeiou]', '', string))

def run_generator():
    with open('palavras.txt') as lista_palavras:
        for palavra in lista_palavras:
            
            palavra = slugify(palavra)

            if palavra.find('-') >= 0:
                continue

            len_vogais = str(vogais(palavra))
            len_palavra = str(len(palavra))

            if not len_palavra in generator:
                generator[len_palavra] = {}

            if not len_vogais in generator[len_palavra]:
                generator[len_palavra][len_vogais] = []

            if palavra in generator[len_palavra][len_vogais]:
                continue

            generator[len_palavra][len_vogais].append(palavra)
        

if __name__ == '__main__':
    run_generator()
    print(json.dumps(generator, indent=2))
