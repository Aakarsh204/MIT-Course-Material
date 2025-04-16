import nltk
from nltk.corpus import brown
from nltk.tag import hmm

tagged_sents = brown.tagged_sents(tagset = 'universal')

train_data = tagged_sents[:50000]
test_data = tagged_sents[50000:50500]

trainer = hmm.HiddenMarkovModelTrainer()
hmm_model = trainer.train_supervised(train_data)

accuracy = hmm_model.accuracy(test_data)
print(f'Accuracy: {accuracy:.2f}')

sentence = "The quick brown fox jumped over the lazy dog".split()
tagged = hmm_model.tag(sentence)
print("Tagged Sentence: ", tagged)
