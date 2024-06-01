"""This module provides encapsulate way to ingest files."""
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor
from common.exceptions import InvalidFile

from .IngestorInterface import IngestorInterface

class Ingestor(IngestorInterface):
    """A class to parse files using different ingestors based on their extensions."""

    ingestors = [CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path: str):
        """Parse a file using the appropriate ingestor based on its extension.

        Args:
            path (str): The path to the file to be parsed.

        Returns:
            list: A list of parsed objects from the file, using the appropriate ingestor.

        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise InvalidFile('Kind of this file does not supported')
