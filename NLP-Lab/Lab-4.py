import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

def n_grams(string, n = 2):
    words = word_tokenize(string)
    n_gram = ngrams(words, n)
    return list(n_gram)

if __name__ == '__main__':
    string = input("Enter the sentence to tokenize\n")
    bigrams = n_grams(string)
    N = len(bigrams)
    hmap = Counter(bigrams)
    print("Bigram Frequencies")
    for pair in hmap:
        print(pair, " ", hmap[pair])

    print("Bigram Probabilities")
    for pair in hmap:
        print("P[", pair, "] : ", hmap[pair] / N)

    print("Reversed Bigrams")
    bigrams_r = bigrams[::-1]

    for pair in bigrams:
        print(pair[::-1])



