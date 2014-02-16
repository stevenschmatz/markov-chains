import random

class Markov(object):
	def __init__(self, open_file):
		self.open_file = open_file
		self.cache = {}

	def Get_Words(self):
		file_text = self.open_file.read()
		return file_text.split()

	def Triples(self):
		self.words = self.Get_Words()
		if len(self.words)<3:
			return
		for i in range(len(self.words)-2):
			yield (self.words[i], self.words[i+1], self.words[i+2])

	def Generate_Database(self):
		for w1, w2, w3 in self.Triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
		print self.cache


MyMarkov = Markov(open('ee.txt', 'r'))
MyMarkov.Generate_Database()