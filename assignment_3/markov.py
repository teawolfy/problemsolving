import random
import os.path
from imdbpie import Imdb
imdb = Imdb()

class Markov():

    def __init__(self, text):
        self.cache = {}
        self.text = text
        self.words = self.text_to_words()
        self.size = len(self.words)
        self.database()

    def text_to_words(self):
        """Splits the text into its individual words"""
        #self.text.seek[0]
        data = self.text.read()
        words = data.split()
        return words

    def doubles(self):
        """Generates sets of two words from the text"""
        if self.size < 2:
            return
        for i in range(self.size - 2):
            yield (self.words[i], self.words[i+1])

    def database(self):
        """Adds the first two words of each triple to the cache as keys, and the third word as the value"""
        for word1, word2 in self.doubles():
            key = (word1)
            if key in self.cache:
                self.cache[key].append(word2)
            else:
                self.cache[key] = [word2]

    def generate_markov_text(self, size = 30):
        """Generates Markov text 

        Randomly chooses a seed word, and randomly picks a word that has been found in the doubles cache to come after the seed
        Repeats this process for however long the review is required to be
        """
        if self.size > 3:
            seed = random.randint(0, self.size - 3)
        else:
            seed = 1
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        word1, word2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(word1)
            word1, word2 = word2, random.choice(self.cache[(word2)])
        gen_words.append(word2)
        return ' '.join(gen_words)

def get_reviews(title, amount = 10):
    """Writes a file containing the best reviews of a movie given the title"""
    reviews = []
    search = imdb.search_for_title(title)[0]
    movie_id = search['imdb_id']
    rev = imdb.get_title_reviews(movie_id, max_results = amount)
    for review in rev:
        reviews.append(review.text)
    rev_text = ' '.join(reviews)
    f_out = open('%s Reviews.txt' %(title), 'w', encoding = 'utf-8')
    f_out.write(rev_text)
    f_out.close()

def generate_review(title, length, review_amount):
    """Generates a movie review using the IMDB reviews as a body and the Markov text generator"""
    if os.path.isfile('%s Reviews.txt' %(title)) == False:
        get_reviews(title, amount = review_amount)
    file_ = open('%s Reviews.txt' %(title))
    markov = Markov(file_)
    return markov.generate_markov_text(size = length)

def main():
    print(generate_review('Black Swan', 40, 50))


if __name__ == '__main__':
    main()
