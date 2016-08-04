import random
articles = ["The ", "A ", "In ", "An ", "At ", "How ", "Our ", "My ", "All ", "To "]
adjectives = ["Stinky ", "Fluffy ", "cuddly ", "jittery ", "angry ", "old ", "terrible ", "basic ", "dizzy ", "bite-sized "]
nouns = ["hats ", "cats ", "kidneys ", "bags ", "pencils ", "joomlas ", "generators ", "pandas ", "dancers "]
articles_length = len(articles)
adjectives_length = len(adjectives)
nouns_length = len(nouns)
random_index = random.randint(0, articles_length -1)
random_index = random.randint(0, adjectives_length -1)
random_index = random.randint(0, nouns_length -1)
for i in range(10):
	print(articles[random_index], adjectives[random_index], nouns[random_index])
	random_index = random.randint(0, articles_length -1)
	random_index = random.randint(0, adjectives_length -1)
	random_index = random.randint(0, nouns_length -1)