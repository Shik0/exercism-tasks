import string

def is_pangram(sentence):
    return set(letter.lower() for letter in sentence if letter.isalpha()) == set(string.ascii_lowercase)
