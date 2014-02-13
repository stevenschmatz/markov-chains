import random

class Markov(object):
	
	def __init__(self, open_file):
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()
		
	
	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words
		
	
	def triples(self):
		""" Generates triples from the given data string. So if our string were
				"What a lovely day", we'd generate (What, a, lovely) and then
				(a, lovely, day).
		"""
		
		if len(self.words) < 3:
			return

		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])
			
	def database(self):
		for w1, w2, w3 in self.triples():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]
				
	def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size-3)
		seed_word, next_word = self.words[seed], self.words[seed+1]
		w1, w2 = seed_word, next_word
		gen_words = []
		for i in xrange(size):
			gen_words.append(w1)
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words)
			
def condition(word):
	end_line_chars = {".": 0.7, ',': 0.4}
	every_other_char = 0.05
	ending = list(word)[len(list(word))-1]
	if ending in end_line_chars:
		if random.uniform(0,1) < end_line_chars[ending]:
			return True
	if random.uniform(0,1) < every_other_char:
		return True
	return False

def generate_poetry(string):
	words = string.split(' ')
	new_word_list = []
	for word in words:
		if condition(word):
			new_word_list.append((word+"\n").lower())
		else:
			new_word_list.append(word.lower())
	return " ".join(new_word_list)

def get_title(list_of_words, length_threshold):
	title = random.choice(list_of_words)
	while True:
		if len(list(title))>length_threshold:
			break
		title = random.choice(list_of_words)
	return title


file_ = open('les_miserables.txt','r')
MyMarkov = Markov(file_)
raw_text = MyMarkov.generate_markov_text(size=100)


title = get_title(MyMarkov.file_to_words(), 10).upper()
print title+"\nSteven Schmatz\n==========="+ "\n "+ generate_poetry(raw_text)