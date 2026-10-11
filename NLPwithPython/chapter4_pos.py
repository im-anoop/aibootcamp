import spacy

nlp = spacy.load("en_core_web_sm")

text = "Virat Kohli plays cricket in India."

doc = nlp(text)

print("POS Tagging:")
for token in doc:
    print(token.text, token.pos_)

print("\nNamed Entity Recognition:")
for ent in doc.ents:
    print(ent.text, ent.label_)
    
# Named entity recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.
import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Microsoft opened a new office in Mumbai.
Google was founded in September 1998.
"""

doc = nlp(text)
print("Named entities:\n")
for entity in doc.ents:
    print(
        "Text:", entity.text,
        "| Label:", entity.label_,
        "| Description:", spacy.explain(entity.label_)
    )