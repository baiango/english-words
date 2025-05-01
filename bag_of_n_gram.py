file_names = [
	"art",
	"business_money",
	"communication_personality",
	"crime_punishment",
	"education",
	"environment",
	"families_children",
	"food_diet",
	"government",
	"health",
	"housing_buildings_urban_planning",
	"language",
	"leisure",
	"media_advertising",
	"reading",
	"society",
	"space_exploration",
	"sports_exercise",
	"technology",
	"tourism and travel",
	"transport",
	"work",
]

save_names = [
	"unigram",
	"bigram",
	"trigram",
	"four_gram",
]

def split_sentences(file_names):
	for n in file_names:
		with open(n + '.txt', 'r') as f:
			words = f.read().split()
			for word in words:
				if any(word.find(s) != -1 for s in ["$", ".com", "https://"]):
					continue
				if any(c.isalpha() for c in word):
					yield word

def save_n_gram(words_count, file_name):
	# Sort words_count by values (word counts) in descending order
	sorted_words_count = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

	filtered_words_count = [
		(w, c) for w, c in sorted_words_count
		if w in ["a", "I"]
		or len(w) > 1
		and c > 1
	]

	with open(file_name + '.txt', 'w') as o:
		for w in filtered_words_count:
			o.write(str(w) + "\n")

saved_words = list(split_sentences(file_names))
words_counts = []

words_count = {}
for w in saved_words:
	clean_word = w.strip(',."\'();:*?!<>').rstrip('-')
	words_count[clean_word] = words_count.get(clean_word, 0) + 1
words_counts.append(words_count)

for n in range(2, 5):
	words_count = {}
	for i in range(len(saved_words) - n + 1):
		n_gram = tuple(saved_words[i:i+n])
		words_count[n_gram] = words_count.get(n_gram, 0) + 1
	words_counts.append(words_count)

for i, wc in enumerate(words_counts):
	save_n_gram(wc, save_names[i])
