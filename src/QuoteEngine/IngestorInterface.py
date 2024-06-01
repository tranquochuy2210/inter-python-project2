"""This module provide an abstract base class representing an ingestor interface for parsing files."""
from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """An abstract base class representing an ingestor interface for parsing files."""

    allowed_extensions = ['csv', 'docx', 'pdf', 'txt']
    
    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the given file path can be ingested based on its extension.

        Args:
            path (str): The path to the file to be checked.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Abstract method to parse a file.

        This method must be implemented by subclasses.

        Args:
            path (str): The path to the file to be parsed.

        Returns:
            list: A list of parsed objects from the file.
        """
        pass
