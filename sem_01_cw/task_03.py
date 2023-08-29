# Задание No3
# 📌 Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/<int:num_1>/<int:num_2>')
def calculate(num_1: int, num_2: int):
    return str(num_1 + num_2)


if __name__ == '__main__':
    app.run()
