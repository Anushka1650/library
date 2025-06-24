from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    with sqlite3.connect("library.db") as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                author TEXT NOT NULL
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS issued (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                book_title TEXT NOT NULL
            )
        ''')
init_db()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = request.form['book']
        author = request.form['author']
        with sqlite3.connect("library.db") as conn:
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book, author))
                conn.commit()
            except sqlite3.IntegrityError:
                return "Book already exists in the library."
        return redirect('/books')
    return render_template('add.html')

@app.route('/books')
def books():
    with sqlite3.connect("library.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT title, author FROM books")
        books = cur.fetchall()
    return render_template('books.html', books=books)

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    if request.method == 'POST':
        name = request.form['name']
        book = request.form['book']
        with sqlite3.connect("library.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM books WHERE title=?", (book,))
            data = cur.fetchone()
            if data:
                cur.execute("DELETE FROM books WHERE title=?", (book,))
                cur.execute("INSERT INTO issued (name, book_title) VALUES (?, ?)", (name, book))
                conn.commit()
                return redirect('/track')
            else:
                return "Book not available or already issued."
    return render_template('borrow.html')

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        name = request.form['name']
        book = request.form['book']
        with sqlite3.connect("library.db") as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM issued WHERE name=? AND book_title=?", (name, book))
            cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book, "Unknown"))
            conn.commit()
        return redirect('/books')
    return render_template('return.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        book = request.form['book']
        author = request.form['author']
        with sqlite3.connect("library.db") as conn:
            cur = conn.cursor()
            try:
                cur.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book, author))
                conn.commit()
            except sqlite3.IntegrityError:
                return "Book already exists."
        return redirect('/books')
    return render_template('donate.html')

@app.route('/track')
def track():
    with sqlite3.connect("library.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, book_title FROM issued")
        records = cur.fetchall()
    return render_template('track.html', records=records)

if __name__ == "__main__":
    app.run()
