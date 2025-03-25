import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

def pos_tagging(text):
    return [(token.text, token.pos_) for token in nlp(text)]

def analyze_text(text):
    doc = nlp(text)
    return {
            "pos_tags": [(token.text, token.pos_) for token in doc],
            "dependencies": [(token.text, token.dep_, token.head.text) for token in doc], 
            "noun_phrases": [chunk.text for chunk in doc.noun_chunks],
            "named_entities": [(ent.text, ent.label_) for ent in doc.ents]
    }

def visualize(text):
    doc = nlp(text)
    displacy.serve(doc, style='dep')

def chunking_noun_phrases(text):
    doc = nlp(text)
    return [" ".join([token.text for token in chunk]) for chunk in doc.noun_chunks]

def multilingual_analysis(text, lang = "en_core_web_sm"):
    model = spacy.load(lang)
    doc = model(text)
    return[(token.text, token.pos_) for token in doc]

if __name__ == '__main__':
    text = "Apple is looking at buying U.K. startups for $1 billion."
    print(analyze_text(text))
    visualize(text)
