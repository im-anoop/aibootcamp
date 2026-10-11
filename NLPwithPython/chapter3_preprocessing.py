# Lowercasing text
#Computers can treat uppercase and lowercase versions of a word as different strings.

text = "I LOVE MY NEW LAPTOP!"
clean_text = text.lower()
print("Clean text:", clean_text)

#Remove extra spaces and punctuation
text = " I LOVE this laptop!!! "

#Python's .strip() removes whitespace from the beginning and end.
#split() followed by " ".join(...) also collapses repeated whitespace between words.
clean_text = text.strip()
clean_text = " ".join(clean_text.split())
lower_text = clean_text.lower()
print("Clean text:", clean_text)

#We can use Python's re module to remove punctuation characters.
import re

text = "Wow!!! This rug is amazing, isn't it?"

clean_text = re.sub(r"[^\w\s]", " ", text)
clean_text = " ".join(clean_text.split())

print(clean_text)

#Remove stop words

import spacy

nlp = spacy.load("en_core_web_sm")

text = "The Desk is in the living room."
doc = nlp(text)

remaining_words = [
    token.text
    for token in doc
    if not token.is_stop and not token.is_punct
]

print(remaining_words)

#Stemming and lemmatization
#Lemmatization: find the base word
#Stemming uses rules to remove word endings. It can produce fragments that aren't proper words.

#Lemmatization: find the base word
#Lemmatization tries to return a recognized dictionary form, called a lemma, using linguistic information.

# for example this is one of the most important concepts in text preprocessing.
# Imagine these words:
#(connect,connected,connecting,connection)
#They are related, but they aren't identical.

#lemmatization with spaCy

import spacy

nlp = spacy.load("en_core_web_sm")

text = "The cats were running and the children ate better meals."
doc = nlp(text)

for token in doc:
    if not token.is_punct:
        print(token.text, "->", token.lemma_)