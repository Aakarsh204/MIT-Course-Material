from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re

def nlp(string):
    tokens = word_tokenize(string)
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]
    print("Original Tokens:", tokens)
    print("Filtered Tokens (without stopwords):", filtered_tokens)
    print("Stemmed Tokens:", stemmed_tokens)
    print("Lemmatized Tokens:", lemmatized_tokens)

def custom_tokenizer(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text.lower())
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    processed_tokens = []
    for token in tokens:
        stemmed = stemmer.stem(token)
        lemmatized = lemmatizer.lemmatize(stemmed)
        processed_tokens.append(lemmatized)
    
    print("Processed Tokens:", processed_tokens)


if __name__ == '__main__':
    string = input("Enter the sentence\n")
    nlp(string)
    custom_tokenizer(string)
