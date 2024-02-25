words = ["hello", "hey", "goodbye", "yo", "yes"]

for item in words: 
      print(item)

def print_upper_words(words):
    for word in words:
        print(word.upper())



def print_upper_words_e(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())



def print_words_starting_with_given_letters(words, letters):
    for word in words:
        if word.startswith(tuple(letters)):
            print(word.upper())


