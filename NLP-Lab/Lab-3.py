import random

def split_into_pairs(word):
    print("Pair-wise Split")
    for i in range(1, len(word)):
        first = word[:i]
        last = word[i:]
        print(first, "+", last)

def generate_affix(word):
    print("Prefixes")
    for i in range(1, len(word)):
        print(word[:i])
    print("Suffixes")
    for i in range(len(word)-1, 0, -1):
        print(word[i:])

def random_split(word):
    print("Random Splits")
    for i in range(1, len(word)):
        x = random.randint(1, len(word)-1)
        first = word[:x]
        last = word[x:]
        print(first, '+', last)

if __name__ == '__main__':
    word = input("Enter the word\n")
    split_into_pairs(word)
    generate_affix(word)
    random_split(word)
