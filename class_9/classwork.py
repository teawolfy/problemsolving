fin = open('words.txt')
line = repr(fin.readline())
# https://docs.python.org/3/library/functions.html#repr

fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)


def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

    pass

def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    if 'e' in word:
        return False
    else:
        return True

def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in forbidden:
        if letter in word:
            return False
    return True
    pass

def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True
    pass

def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    # for letter in required:
    #     if not letter in word:
    #         return False
    # return True
    return uses_only(required, word)
    pass

def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    for i in range(1, len(word)):
        if ord(word[i].lower()) <= ord(word[i-1].lower()):
            return False
    return True
    pass

print(is_abecedarian('abs'))
print(is_abecedarian('college'))