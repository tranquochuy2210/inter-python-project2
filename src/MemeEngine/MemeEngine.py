"""This module provides Meme with quotes."""

from PIL import Image, ImageDraw, ImageFont
from random import randint
import os

class MemeEngine:
    """A class to generate memes with text greetings."""

    def __init__(self, output_dir: str) -> None:
        """Initialize the Meme object with the output directory.

        Args:
            output_dir (str): The directory where generated memes will be saved.
        """
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir
    
    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Generate a postcard with a text greeting.

        Args:
            img_path (str): The path to the image to be used for the postcard.
            text (str): The text to be included in the postcard.
            author (str): The author of the text.
            width (int, optional): The width of the postcard. Defaults to 500.

        Returns:
            str: The path to the generated postcard image.
        """
        quote = f'{text} - {author}'
        out_path = f'{self.output_dir}/{randint(1,100000000)}.png'
        font = ImageFont.load_default()
        print(img_path)
        img = Image.open(img_path)
        width = min(width, 500)
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        draw = ImageDraw.Draw(img)
        quote_height = randint(0, height)
        quote_width = randint(0, width-70)
        def wrap_text(text, font, max_width):
            lines = []
            words = text.split()
            line = ''
            for word in words:
                # Check the width of the line with the new word
                if draw.textbbox((0, 0), line + word, font=font)[2] <= max_width:
                    line += word + ' '
                else:
                    lines.append(line.strip())
                    line = word + ' '
            lines.append(line.strip())  # Add the last line
            return lines
        lines = wrap_text(quote, font, 70)
        for line in lines:
            draw.text((quote_width, quote_height), line, font=font, fill="black")
            quote_height += draw.textbbox((0, 0), line, font=font)[3]
        img.save(out_path)
        return out_path
