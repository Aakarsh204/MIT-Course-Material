import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize

def tokenize(string):
    print(sent_tokenize(string))
    print(word_tokenize(string))

def split(string):
    pattern = r"[^\w]+"
    result = re.split(pattern, string)
    final = [x for x in result if x != ""]
    print(final)

def extract_date(string):
    pattern = r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}"
    result = re.findall(pattern, string)
    print(result)

def extract_phno(string):
    pattern = r" ^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    result = re.findall(pattern, string)
    print(result)

if __name__ == '__main__':
    print("Enter the string")
    string = input()
    print("Enter what you want to do to the string")
    print('''1. Tokenize
2. Split sentence
3. Extract date
4. Extract phone number''')
    choice = int(input())
    match choice:
        case 1: 
            tokenize(string)
        case 2:
            split(string)
        case 3:
            extract_date(string)
        case 4:
            extract_phno(string)
