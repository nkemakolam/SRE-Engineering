import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from ebooklib import epub
from bs4 import BeautifulSoup

# Function to extract text from EPUB file
def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    text = ""
    for item in book.items:
        if item.get_type() == 9 :
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text += soup.get_text()
    return text

# Function for Named Entity Recognition using nltk
def get_entities_nltk(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    entities = ne_chunk(tagged)
    named_entities = []
    for subtree in entities:
        if isinstance(subtree, nltk.tree.Tree):
            entity = " ".join([word for word, pos in subtree.leaves()])
            entity_type = subtree.label()
            named_entities.append((entity, entity_type))
    return named_entities

# Function to generate user-friendly explanations for entities
def generate_explanations(entities):
    explanations = {}
    for text, entity_type in entities:
        if entity_type == "GPE":  # Geography (cities, countries)
            explanations[text] = f"Information about {text}..."
        elif entity_type == "PERSON":
            explanations[text] = f"Biographical information about {text}..."
        # Add more rules or templates for other entity types if needed
    return explanations

# Main function to process the EPUB file
def main():
    epub_path = "./accessible_epub_3.epub"  # Update with your EPUB file path
    text = extract_text_from_epub(epub_path)
    entities = get_entities_nltk(text)
    explanations = generate_explanations(entities)

    for entity, explanation in explanations.items():
        print(f"{entity}: {explanation}")

if __name__ == "__main__":
    main()


