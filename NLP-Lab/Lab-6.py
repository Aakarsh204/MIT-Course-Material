import re

def remove_noise(text: str) -> None:
    text = re.sub(r'#\w+', lambda m: m.group()[1:], text)
    text = re.sub(r'@\w+', lambda m: m.group()[1:], text)
    text = re.sub(r'[^\w\s\']', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    print("Noise Removed Text:", text)

def remove_emojis(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        "]+", flags=re.UNICODE)
    print("Emoji Removed Text:", emoji_pattern.sub(r'', text)

def normalize(text):
    text = re.sub(r'\s+', ' ', text).strip()
    print("Normalized Text:", text.lower())

if __name__ == '__main__':
    string = input("Enter the string\n")
    remove_noise(string)
    remove_emojis(string)
    normalize(string)
    
