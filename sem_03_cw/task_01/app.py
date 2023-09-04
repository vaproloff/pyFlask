# Задание No1
# 📌 Создать базу данных для хранения информации о студентах университета.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# 📌 В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# 📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.

import random

from flask import Flask, render_template
from models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sem_03_task_01.db'
db.init_app(app)


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_db():
    for i in range(3):
        faculty = Faculty(
            name=f'Faculty_{i}'
        )
        db.session.add(faculty)
    db.session.commit()

    for i in range(10):
        student = Student(
            first_name=f'Name_{i}',
            last_name=f'Last_Name_{i}',
            age=random.randint(18, 23),
            gender=random.choice(['male', 'female']),
            id_faculty=random.randint(1, 3)
        )
        db.session.add(student)
    db.session.commit()

    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
