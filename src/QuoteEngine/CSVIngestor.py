"""This module provides functionality to ingest CSV files."""
from .IngestorInterface import IngestorInterface
from typing import List
import pandas
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """A class to ingest CSV files containing quotes and authors."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a CSV file containing quotes and authors.

        Args:
            path (str): The path to the CSV file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing the quotes and authors.
        
        Raises:
            Exception: If the file cannot be ingested.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest CSV file.')

        df = pandas.read_csv(path, header=0)
        quotes = []
        for _, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)
        return quotes
