import re

slang_dict = {
    "u": "you",
    "r": "are",
    "omg": "oh my god",
    "lol": "laugh out loud",
    "idk": "I don't know",
    "btw": "by the way"
}

emoji_dict = {
    ":)": "happy",
    ":-)": "happy",
    ":(": "sad",
    ":-(": "sad",
    ";)": "wink",
    ";-)": "wink",
}

def replace_slang_and_emojis(text):
    words = text.split()
    replaced_text = " ".join([slang_dict.get(word.lower(), word) for word in words])
    
    for emoji, replacement in emoji_dict.items():
        replaced_text = replaced_text.replace(emoji, replacement)
    
    replaced_text = re.sub(r'\s+', ' ', replaced_text)  
    replaced_text = re.sub(r'([?!,.])\1+', r'\1', replaced_text) 
    replaced_text = re.sub(r'\s([?!,.])', r'\1', replaced_text)
    
    return replaced_text

test_texts = [
    "omg!!! u r amazing :)",
    "idk... what's happening :(",
    "btw, lol u r great ;) :-)",
    "hello!!!    world!!!",
]

for text in test_texts:
    print("Original:", text)
    print("Processed:", replace_slang_and_emojis(text))
    print()

def standardize_text(text):
    words = text.split()
    standardized_text = " ".join([slang_dict.get(word.lower(), word) for word in words])
    
    standardized_text = re.sub(r'\s+', ' ', standardized_text)
    standardized_text = re.sub(r'([?!,.])\1+', r'\1', standardized_text)  
    standardized_text = re.sub(r'\s([?!,.])', r'\1', standardized_text)     
    standardized_text = standardized_text.lower()
    
    return standardized_text


test_sentence = "OMG!!! This is sooo cool!!! BTW, u r amazing :)!!!"
print("Original:", test_sentence)
print("Standardized:", standardize_text(test_sentence))
