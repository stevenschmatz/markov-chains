__author__ = 'stevenschmatz'

import random, string

my_path = 'poetry.txt'


class Markov(object):
    def __init__(self, path):
        self.f = open(path)
        self.text = self.f.read()
        self.cache = {}

    def get_triples(self):
        for char in xrange(len(list(self.text)) - 2):
            first_two = (self.text[char], self.text[char + 1])
            if first_two not in self.cache:
                self.cache[first_two] = [self.text[char + 2]]
            else:
                self.cache[first_two].append(self.text[char + 2])

    def make_text(self):
        initial_letters = ''
        while True:
            initial_letters = random.choice(self.cache.keys())
            if (initial_letters[0] == string.upper(initial_letters[0])) and (initial_letters[0].isalnum()):
                break
        print initial_letters, random.choice(self.cache[initial_letters])

my_chain = Markov(my_path)
my_chain.get_triples()
my_chain.make_text()