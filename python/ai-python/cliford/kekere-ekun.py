from ebooklib import epub

def extract_text_from_epub(epub_file_path):
    """
    Function to extract text from an EPUB file.

    Parameters:
        epub_file_path (str): The path to the EPUB file.

    Returns:
        str: The extracted text from the EPUB file.
    """
    # Create an EPUB book object
    book = epub.read_epub(epub_file_path)

    # Initialize an empty string to store the extracted text
    extracted_text = ""

    # Iterate through all the spine items in the EPUB book
    for item_id, spine_item in enumerate(book.get_items_of_type(epub.EpubHtml)):
        # Read the content from the spine item and append it to the extracted_text
        extracted_text += spine_item.get_body_content().decode('utf-8', 'ignore')

    # Return the extracted text
    return extracted_text


# Example usage:
if __name__ == "__main__":
    epub_file_path = "./accessible_epub_3.epub"
    extracted_text = extract_text_from_epub(epub_file_path)
    print(extracted_text)
    
