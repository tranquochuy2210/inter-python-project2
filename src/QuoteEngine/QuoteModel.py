"""Provide QuoteModel."""
class QuoteModel:
    """Represents a quote along with its author.

    Attributes:
        quote (str): The text of the quote.
        author (str): The author of the quote.
    """

    def __init__(self, body: str, author: str) -> None:
        """Initialize a QuoteModel object with the given quote and author.

        Args:
            quote (str): The text of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author
    
    def __str__(self) -> str:
        """Return a string representation of the QuoteModel object.

        Returns:
            str: A string containing the quote text and author.
        """
        return f'"{self.body}" - {self.author}'
