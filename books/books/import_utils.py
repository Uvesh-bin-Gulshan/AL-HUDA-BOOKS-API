from docx import  Document
import pandas as pd
from hadith.models import Book,Translation,ContentSection





def import_book_from_word(file_path,book_id,translation_language):

    #load document
    doc=Document(file_path)


    
    #get book and translation
    book=Book.objects.get(id=book_id)
    translation,created=Translation.object.get_or__create(book=book,language=translation_language)


        # Initialize counters
    index, sub_index, page_number = 1, 1, 1
    sections_imported = 0

    for paragraph in doc.paragraphs:
        if paragraph.text.strip():  # Only process non-empty paragraphs
            ContentSection.objects.create(
                translation=translation,
                index=str(index),
                sub_index=str(sub_index),
                content=paragraph.text,
                page_number=page_number
            )
            sub_index += 1
            page_number += 1
            sections_imported += 1

    return sections_imported



def import_book_from_excel(file_path, book_id, translation_language):
    """
    Imports book content from an Excel file into the database.

    Args:
        file_path (str): Path to the Excel file.
        book_id (UUID): ID of the Book model instance.
        translation_language (str): Language of the translation.

    Returns:
        int: Number of sections imported.
    """
    # Load Excel file
    df = pd.read_excel(file_path)
    
    # Get the book and its translation
    book = Book.objects.get(id=book_id)
    translation, created = Translation.objects.get_or_create(book=book, language=translation_language)

    # Track imported sections
    sections_imported = 0

    # Iterate over rows and create ContentSections
    for _, row in df.iterrows():
        ContentSection.objects.create(
            translation=translation,
            index=row['Index'],
            sub_index=row.get('Sub Index', ''),
            content=row['Content'],
            page_number=row['Page Number']
        )
        sections_imported += 1

    return sections_imported