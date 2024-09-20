words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

# Afficher tuple de mots et leurs voyelles

tuples_words_vowels = [(word, len([letter for letter in word if letter in "aeiou"])) for word in words]
print(tuples_words_vowels)

