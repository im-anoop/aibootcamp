# Tokenization is the process of breaking a stream of text up into words, phrases, 
# symbols, or other meaningful elements called tokens. The list of tokens becomes 
# input for further processing such as parsing or text mining.
#Tokenization using spaCy

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")  
sentence = "I love learning NLP!"

#analyze the sentence using the NLP model
doc = nlp(sentence)

# print every token in the sentence
print("Tokens:")
for token in doc:
    print(token.text)
print("Total tokens:", len(doc))
    