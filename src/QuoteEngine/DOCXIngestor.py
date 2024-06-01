"""This module provides functionality to ingest DOCX files."""
from .IngestorInterface import IngestorInterface
from typing import List
import docx
from .QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
    """A class to ingest DOCX files containing quotes and authors."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a DOCX file containing quotes and authors.

        Args:
            path (str): The path to the DOCX file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing the quotes and authors.
        
        Raises:
            Exception: If the file cannot be ingested.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest DOCX file.')

        doc = docx.Document(path)
        quotes = []
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                if len(parse) < 2:
                    continue
                quote = parse[0].strip().strip('"')
                author = parse[1]
                quote_instance = QuoteModel(quote, author)
                quotes.append(quote_instance)
        return quotes
