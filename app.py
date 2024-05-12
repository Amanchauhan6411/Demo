from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {"id":1,"title":"Book 1", "author":"Author1"},
    {"id":2,"title":"Book 2", "author":"Author2"},
    {"id":3,"title":"Book 3", "author":"Author3"},
    {"id":4,"title":"Book 4", "author":"Author4"},
    {"id":5,"title":"Book 5", "author":"Author5"},
    {"id":6,"title":"Book 6", "author":"Author6"},
    {"id":7,"title":"Book 7", "author":"Author7"},
]

@app.route('/', methods=['GET'])
def home_page():
    return 'home page'

# route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# route to get specific book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
        
    return jsonify({'error':'Book not found'})


# route to add a new book
@app.route('/books', methods=['POST'])
def add_books():
    new_book = {
        "id":request.json['id'],
        "title":request.json['title'],
        "author":request.json['author'],
    }
    books.append(new_book)
    return jsonify({'message':'Book added succesfully'})


# route to update and existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return jsonify({'message':'Book update succesfully'})
        
    return jsonify({'error':'Book not found'})


# route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message':'Book deleted succesfully'})
        
    return jsonify({'error':'Book not found'})