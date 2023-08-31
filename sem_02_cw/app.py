from pathlib import PurePath, Path
from flask import Flask, render_template, url_for, request, abort, redirect, flash
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'3891f989b75a5b6e8f5f8cab6d1431b865a05acc126ff7e1cae4ce028df65413'

USER = {
    'login': 'Vasiliy',
    'password': 'pass123'
}


@app.route('/')
def index():
    return render_template('index.html')


# Задание No1
# 📌 Создать страницу, на которой будет кнопка "Нажми меня",
#    при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.

@app.route('/task_01/')
def task_01():
    return f'Привет, Вася'


# Задание No2
# 📌 Создать страницу, на которой будет изображение и ссылка на другую страницу,
#    на которой будет отображаться форма для загрузки изображений.

@app.route('/task_02/', methods=['GET', 'POST'])
def task_02():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {escape(file_name)} загружен на сервер'

    context = {
        'title': 'Задание 2',
    }
    return render_template('task_02.html', **context)


# Задание No3
# 📌 Создать страницу, на которой будет форма для ввода логина и пароля
# 📌 При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля
#    и переход на страницу приветствия пользователя или страницу с ошибкой.

@app.route('/task_03/', methods=['GET', 'POST'])
def task_03():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == USER['login'] and password == USER['password']:
            return 'Вход выполнен успешно'
        else:
            return 'Ошибка при авторизации'
    context = {
        'title': 'Задание 3',
    }
    return render_template('task_03.html', **context)


# Задание No4
# 📌 Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

@app.route('/task_04/', methods=['GET', 'POST'])
def task_04():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Количество слов: {len(text.split())}'
    context = {
        'title': 'Задание 4',
    }
    return render_template('task_04.html', **context)


# Задание No5
# 📌 Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
#    (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# 📌 При нажатии на кнопку будет произведено вычисление результата выбранной операции
#    и переход на страницу с результатом.

@app.route('/task_05/', methods=['GET', 'POST'])
def task_05():
    if request.method == 'POST':
        a = request.form.get('num-a')
        b = request.form.get('num-b')
        operation = request.form.get('operation')
        return f'Результат: {eval(f"{a} {operation} {b}")}'
    context = {
        'title': 'Задание 5',
    }
    return render_template('task_05.html', **context)


# Задание No6
# 📌 Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом
#    или на страницу с ошибкой в случае некорректного возраста.

@app.errorhandler(403)
def forbidden(e):
    context = {
        'title': 'Доступ запрещён по возрасту',
        'url': request.base_url
    }
    return render_template('403.html', **context)


@app.route('/task_06/', methods=['GET', 'POST'])
def task_06():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        try:
            age_num = int(age)
        except ValueError as e:
            return 'Ошибка проверки возраста'
        if age_num >= 18:
            return f'Результат:\nИмя: {name}, возраст: {age}'
        else:
            abort(403)
    context = {
        'title': 'Задание 6',
    }
    return render_template('task_06.html', **context)


# Задание No7
# 📌 Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено перенаправление на страницу с результатом,
#    где будет выведено введенное число и его квадрат.


@app.route('/task_07/<int:number>/')
def task_07_result(number):
    return f'Число: {number}, его квадрат: {number ** 2}'


@app.route('/task_07/', methods=['GET', 'POST'])
def task_07():
    if request.method == 'POST':
        num = request.form.get('number')
        return redirect(url_for('task_07_result', number=int(num)))
    context = {
        'title': 'Задание 7',
    }
    return render_template('task_07.html', **context)


# Задание No8
# 📌 Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
#    где будет выведено "Привет, {имя}!".

@app.route('/task_08/', methods=['GET', 'POST'])
def task_08():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}', 'success')
        return redirect(url_for('task_08'))
    context = {
        'title': 'Задание 8',
    }
    return render_template('task_08.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
