from epublib import epub
from bs4 import BeautifulSoup
import spacy

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    text = ""
    for item in book.items:
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text += soup.get_text()
    return text



def get_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def generate_explanations(entities):
    explanations = {}
    for text, entity_type in entities:
        if entity_type == "GPE":  # Geography (cities, countries)
            explanations[text] = f"Information about {text}..."
        elif entity_type == "PERSON":
            explanations[text] = f"Biographical information about {text}..."
        # Add more rules or templates for other entity types if needed
    return explanations
def main():
    epub_path = "path/to/your/epub/file.epub"
    text = extract_text_from_epub(epub_path)
    entities = get_entities(text)
    explanations = generate_explanations(entities)

    for entity, explanation in explanations.items():
        print(f"{entity}: {explanation}")

if __name__ == "__main__":
    main()

