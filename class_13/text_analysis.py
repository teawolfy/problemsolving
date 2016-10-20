import random
import string
remove_punct_map = dict.fromkeys(map(ord, string.punctuation))

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        for word in line.split():
            word = word.lower()
            word = word.translate(remove_punct_map)
            hist[word] = hist.get(word, 0) + 1
        pass

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())
    pass

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)
    pass

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    temp = []
    for word, freq in hist.items():
        temp.append((freq, word))
    temp.sort()
    temp.reverse()
    return temp
    pass

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    pairs = most_common(hist)
    return pairs[:10]
    pass

def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    temp = {}
    for key, value in d1.items():
        if key not in d2.keys():
            temp[key] = value
    return temp
    pass

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    total = sum(weight for choice, weight in hist.items())
    rando = random.uniform(0, total)
    sorter = 0
    for choice, weight in hist.items():
        if sorter + weight >= rando:
            return choice
        sorter += weight
    pass

def main():
    hist = process_file('Dunwich.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()