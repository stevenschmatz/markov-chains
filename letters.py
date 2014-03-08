__author__ = 'stevenschmatz'

import random, string

my_path = 'les_miserables.txt'


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

    def make_text(self, length=100):
        initial_letters = ''
        while True:
            initial_letters = random.choice(self.cache.keys())
            if (initial_letters[0] == string.upper(initial_letters[0])) and (initial_letters[0].isalnum()):
                break
        self.new_words = [initial_letters[0], initial_letters[1], random.choice(self.cache[initial_letters])]
        for i in xrange(length):
            num_letters = len(self.new_words)
            self.new_words.append(
                random.choice(self.cache[(self.new_words[num_letters - 2], self.new_words[num_letters - 1])]))

        return ''.join(self.new_words)


my_chain = Markov(my_path)
my_chain.get_triples()
print my_chain.make_text(length = 500)