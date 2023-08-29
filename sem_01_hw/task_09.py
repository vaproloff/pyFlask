# Задание No9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
#    и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

CATALOG = {
    'clothes': {
        'title': 'Одежда',
        'items': [
            {
                'brand': 'UNIQLO',
                'description': 'Жилет пуховый ультралегкий',
                'img': 'cloth_001.png',
                'price': 4999
            },
            {
                'brand': 'Lyle & Scott',
                'description': 'Футболки 3 шт. Maxwell',
                'img': 'cloth_002.png',
                'price': 4740
            },
            {
                'brand': 'Torae Black',
                'description': 'Худи оверсайз',
                'img': 'cloth_003.png',
                'price': 2990
            },
        ],
    },
    'shoes': {
        'title': 'Обувь',
        'items': [
            {
                'brand': 'adidas Originals',
                'description': 'Кеды GAZELLE',
                'img': 'shoes_001.png',
                'price': 14999
            },
            {
                'brand': 'Ecco',
                'description': 'Кроссовки BIOM FJUEL M',
                'img': 'shoes_002.png',
                'price': 18990
            },
            {
                'brand': 'Native',
                'description': 'Ботинки Fitzsimmons Citylite',
                'img': 'shoes_003.png',
                'price': 15199
            },
        ],
    }
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/catalog/<string:category>/')
def catalog(category):
    if category in CATALOG.keys():
        return render_template('catalog.html', **CATALOG[category])
    else:
        return render_template('404.html')


@app.route('/catalog/<string:category>/<int:item_index>/')
def item(category, item_index):
    print(f'{len(CATALOG[category]) = }')
    print(f'{item_index = }')
    if category in CATALOG.keys() and len(CATALOG[category]['items']) >= item_index:
        return render_template('item.html', **CATALOG[category]['items'][item_index - 1])
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run()
