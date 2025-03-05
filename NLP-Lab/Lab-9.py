import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
import networkx as nx
import matplotlib.pyplot as plt

stop_words = set(stopwords.words("english"))
punct = (',', '"', "'", ".", "!", '?', '&')

def pos_tag(string):
    sents = sent_tokenize(string)
    for sent in sents:
        words = word_tokenize(sent)
        words = [word for word in words if not word in stop_words and not word in punct]
        tagged = nltk.pos_tag(words)

class TextAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    def pos_tagging(self, text):
        tokens = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)
        return pos_tags
    
    def dependency_analysis(self, text):
        doc = self.nlp(text)
        dependencies = {
            'tokens': [token.text for token in doc],
            'dependencies': [(token.text, token.dep_, token.head.text) for token in doc]
        }
        return dependencies
    
    def extract_noun_phrases(self, text):
        doc = self.nlp(text)
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        return noun_phrases
    
    def named_entity_recognition(self, text):
        doc = self.nlp(text)
        entities = {}
        for ent in doc.ents:
            if ent.label_ not in entities:
                entities[ent.label_] = []
            entities[ent.label_].append(ent.text)
        return entities
    
    def visualize_dependency_tree(self, text):
        doc = self.nlp(text)
        G = nx.DiGraph()
        for token in doc:
            G.add_node(token.text, pos=token.pos_)
            if token.dep_ != "ROOT":
                G.add_edge(token.head.text, token.text, label=token.dep_)
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G, k=0.5)
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Dependency Tree")
        plt.axis('off')
        return plt
    
    def analyze_text(self, text):
        return {
            'POS Tags': self.pos_tagging(text),
            'Dependencies': self.dependency_analysis(text),
            'Noun Phrases': self.extract_noun_phrases(text),
            'Named Entities': self.named_entity_recognition(text)
        }

def main():
    analyzer = TextAnalyzer()
    
    sample_text = "Apple Inc. was founded by Steve Jobs in Cupertino, California."
    
    analysis_results = analyzer.analyze_text(sample_text)
    
    print("Part of Speech Tags:")
    for word, tag in analysis_results['POS Tags']:
        print(f"{word}: {tag}")
    
    print("\nDependencies:")
    for token, dep, head in analysis_results['Dependencies']['dependencies']:
        print(f"{token} (depends on {head}) - {dep}")
    
    print("\nNoun Phrases:")
    print(analysis_results['Noun Phrases'])
    
    print("\nNamed Entities:")
    for entity_type, entities in analysis_results['Named Entities'].items():
        print(f"{entity_type}: {entities}")
    
    dep_tree = analyzer.visualize_dependency_tree(sample_text)
    dep_tree.show()

if __name__ == '__main__':
    string = input("Enter the string \n")
    pos_tag(string)
    main()