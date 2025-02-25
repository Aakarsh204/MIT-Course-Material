import re

def remove_digits(string: str) -> None:
    '''
    This function acts as a greedy tokenizer to remove any and all tokens that contain 
    digits in them. Initial tokenization is done by whitespace splitting.
    '''
    tokens = string.split()
    tokens = [token for token in tokens if not re.search(r"\d", token)]
    string = ' '.join(tokens)
    print("Tokens without any digits:", tokens)
    print("Reconstructed String:", string)


def count_digits(string: str) -> None:
    '''
    This function uses the r"\d" regex pattern to count all the digits in a given string.
    '''
    count = 0
    for ch in string:
        if re.search(r"\d", ch):
            count += 1
    print("Total count of digits in the given string:", count)

def print_digits(string: str) -> None:
    '''
    This function used the r"\d" regex pattern to extract and print all digits in a string.
    '''
    tokens = re.findall(r"\d", string)
    print("Extracted Digits:", tokens)

def tokenize(string: str) -> None:
    '''
    This function uses two separate regex patterns to check for the existence of dates
    or emails in the given string and greedily tokenizes it. This means all other
    substrings become the remaining tokens. For example - 
    Input: I was born on 20/04/2004 and I want to own chat@gpt.com!
    Output: ["I was born on ", "20/04/2004", " and I want to own ", "chat@gpt.com", "!"]
    '''
    date = r'\d{1,2}/\d{1,2}/\d{2,4}'
    email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    combined_pattern = f'({date}|{email})'
    tokens = re.split(f'{combined_pattern}', string)
    tokens = [token for token in tokens if token]
    print("Greedy Email/Date Tokens:", tokens)

if __name__ == "__main__":
    string = input("Enter the string\n")
    remove_digits(string)
    count_digits(string)
    print_digits(string)
    tokenize(string)
