from flask import Flask, render_template, request, jsonify, Response
from books import books
import random

app = Flask(__name__)


@app.route("/allbooks", methods = ['GET'])
def returnAllBooks():
    return jsonify(books)

@app.route("/book", methods = ['GET'])
def return_books():
    genre = request.args.get('genre')
    author = request.args.get('author')
    if genre:
        filtered_books = []
        genre = genre.lower()
        for book in books:
            if book['genre'].lower() == genre:
                filtered_books.append(book)
        if len(filtered_books) > 0:
            return jsonify(filtered_books)
        else:
            return jsonify({'error': 'No books available in the specified genre','available_genres': list(filterOptions(books, 'genre'))}), 404
    if author:
        filtered_books = []
        author = author.lower()
        for book in books:
            if book['author'].lower() == author:
                filtered_books.append(book)
        if len(filtered_books) > 0:
            return jsonify(filtered_books)
        else:
            return jsonify({'error': 'No books available for the specified author','available_authors': list(filterOptions(books, 'author'))}), 404    
    return jsonify(random.choice(books))

def filterOptions(books, filter):
    listOfFilters = set()
    for book in books:
        listOfFilters.add(book[filter])
    return listOfFilters


# if __name__ == "__main__":
#     app.run()
    # app.run(host='127.0.0.1', port=5002)
