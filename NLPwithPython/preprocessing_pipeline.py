# Complete preprocessing pipeline for text data using spaCy and regex
import re
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Step 1: Convert to lowercase
    text = text.lower()

    # Step 2: Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Step 3: Normalize whitespace
    text = " ".join(text.split())

    # Step 4: Analyze the text with spaCy
    doc = nlp(text)

    # Step 5: Remove stop words and punctuation
    words = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_space
    ]

    return words


review = "WOW!!! This blog is AMAZING! Visit https://example.com"

result = preprocess_text(review)

print("Original:", review)
print("Processed:", result)