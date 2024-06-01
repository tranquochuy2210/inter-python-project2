import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.IngestorEngine import Ingestor
import random
# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        _quote =Ingestor.parse(file)
        quotes.extend(_quote)
    


    images_path = "./_data/photos/dog/"

    imgs = None
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]
    

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        image_url = request.form['image_url']
        body  = request.form['body']
        author = request.form['author']
        r = requests.get(image_url)
        if r.status_code !=200:
            raise Exception('cannot fetch image_url')
        directory = './tmp'
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, f'{random.randint(1,1000000000000)}.jpg')
        with open(file_path, 'wb') as file:
            file.write(r.content)
        path = meme.make_meme(file_path, body, author)
        os.remove(file_path)
        return render_template('meme.html', path=path)
    except Exception as e:
        print(f'Error when create meme {e}')
        return "Looks like you have mentioned an invalid image URL. Kindly cross-check"


if __name__ == "__main__":
    app.run()
