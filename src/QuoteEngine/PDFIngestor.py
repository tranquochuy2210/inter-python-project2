"""This module provides functionality to ingest PDF files."""

import random
import os
import subprocess
from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor


class PDFIngestor(IngestorInterface):
    """A class to ingest PDF files and convert them into a format suitable for further processing.
    
    This class uses the `pdftotext` utility to convert PDF files to text files, 
    which are then parsed using the `TXTIngestor` class.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """Parse a PDF file and extract its contents."""
        temp_filename = f'{random.randint(1,1000000)}.txt'
        cls.convert_pdf_to_text(path, temp_filename)
        data = TXTIngestor.parse(temp_filename)
        os.remove(temp_filename)
        return data

    @classmethod
    def convert_pdf_to_text(cls, pdf_path, txt_path):
        """Convert a PDF file to a text file using the `pdftotext` utility."""
        try:
            subprocess.run(['pdftotext', '-layout', pdf_path, txt_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Conversion successful.")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e.stderr.decode()}")
