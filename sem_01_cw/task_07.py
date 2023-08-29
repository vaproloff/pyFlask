# Задание No7
# 📌 Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через контекст.
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def news():
    context = {
        'title': 'Новости',
        'news': [
            {
                'title': 'Новость 1',
                'description': 'В Сибири - холодно',
                'create_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
            },
            {
                'title': 'Новость 2',
                'description': 'В Москве - солнечно',
                'create_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
            },
            {
                'title': 'Новость 3',
                'description': 'На Урале мокро',
                'create_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
            },
        ]
    }
    return render_template('task_07.html', **context)


if __name__ == '__main__':
    app.run()
