#exercise 1
def getavailableletters(lettersguessed):
    import string
    possibleletters = list(string.ascii_lowercase)
    for letters in lettersguessed:
        if letters in possibleletters:
            possibleletters.remove(letters)
    availableletters = ''.join(possibleletters)
    return availableletters

print(getavailableletters(['a','c']))