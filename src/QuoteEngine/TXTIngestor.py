"""This module provides functionality to ingest TXT files."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """A class to ingest TXT files containing quotes and authors."""

    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str):
        """Parse a TXT file containing quotes and authors.

        Args:
            path (str): The path to the TXT file to be parsed.

        Returns:
            list: A list of QuoteModel objects representing the quotes and authors.
        """
        quotes = []
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parse = line.split('-')
                if len(parse) < 2:
                    continue
                quote = parse[0].strip().strip('"')
                author = parse[1].strip()
                quote_instance = QuoteModel(quote, author)
                quotes.append(quote_instance)
        return quotes
