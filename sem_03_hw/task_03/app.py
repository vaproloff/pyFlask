# Задание No3
# 📌 Доработаем задача про студентов.
# 📌 Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# 📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
# 📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

import random

from flask import Flask, render_template
from models import db, Student, Grade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Main page'


@app.route('/students/')
def show_students():
    students = Student.query.all()
    return render_template('students.html', students=students)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('DB created.')


@app.cli.command("fill-db")
def fill_db():
    for i in range(1, 6):
        student = Student(
            first_name=f'First_Name_{i}',
            last_name=f'Last_Name_{i}',
            group=f'{random.randint(1, 5)}{random.choice(("A", "B", "C"))}',
            email=f'username_{i}@email.com',
        )
        db.session.add(student)

    for _ in range(20):
        grade = Grade(
            student_id=random.randint(1, 5),
            subject=random.choice(('Maths', 'Literature', 'Physics', 'Chemistry')),
            grade=random.choice(('A', 'B', 'C', 'D', 'E', 'F')),
        )
        db.session.add(grade)

    db.session.commit()
    print('DB filled with data.')


if __name__ == '__main__':
    app.run(debug=True)
