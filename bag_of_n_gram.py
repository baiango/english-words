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

with open('bag_of_n.txt', 'w') as o:
	words_count = {}

	for n in file_names:
		with open(n + '.txt', 'r') as f:
			words = f.read().split()
			for word in words:
				if any(word.find(s) != -1 for s in ["$", ".com", "https://"]):
					continue
				clean_word = word.strip(',."\'();:*?!<>').rstrip('-')
				if any(c.isalpha() for c in word):
					words_count[clean_word] = words_count.get(clean_word, 0) + 1

	# Sort words_count by values (word counts) in descending order
	sorted_words_count = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

	filtered_words_count = [
		(w, c) for w, c in sorted_words_count
		if w in ["a", "I"]
		or len(w) > 1
		and c > 1
	]

	for w in filtered_words_count:
		o.write(str(w) + "\n")
