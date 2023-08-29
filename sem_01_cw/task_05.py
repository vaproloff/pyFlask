# Задание No5
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с заголовком
#    "Моя первая HTML страница" и абзацем "Привет, мир!".

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('task_05.html')


if __name__ == '__main__':
    app.run()
