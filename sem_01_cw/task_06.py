# Задание No6
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def students():
    context = {
        'title': 'Студенты',
        'headers': {
            'name': 'Имя',
            'surname': 'Фамилия',
            'age': 'Возраст',
            'avg_mark': 'Средний балл'
        },
        'students': [
            {
                'name': 'Иван',
                'surname': 'Петров',
                'age': 24,
                'avg_mark': 4.8
            },
            {
                'name': 'Пётр',
                'surname': 'Иванов',
                'age': 22,
                'avg_mark': 3.8
            },
            {
                'name': 'Татьяна',
                'surname': 'Конева',
                'age': 19,
                'avg_mark': 4.0
            },
        ]
    }
    return render_template('task_06.html', **context)


if __name__ == '__main__':
    app.run()
