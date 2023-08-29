# Задание No1
# 📌 Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run()
