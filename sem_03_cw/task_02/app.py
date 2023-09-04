# Задание No2
# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.

import random

from flask import Flask, render_template
from models import db, Book, Author, BookAuthor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_db():
    for i in range(1, 10):
        book = Book(
            title=f'Book_{i}',
            year=random.randint(1900, 2023),
            circulation=random.randint(1, 100)*1000
        )
        db.session.add(book)

    for i in range(1, 15):
        author = Author(
            first_name=f'First_name_{i}',
            last_name=f'Last_Name_{i}'
        )
        db.session.add(author)

    for i in range(1, 15):
        book_author = BookAuthor(
            book_id=random.randint(1,9),
            author_id=random.randint(1, 14)
        )
        db.session.add(book_author)

    db.session.commit()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
