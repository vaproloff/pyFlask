from flask import Flask, request, render_template, abort

# from db import get_blog

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    ...
    result = get_blog(id)
    if result is None:
        abort(404)
    ...


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def page_not_found(e):
    app.logger.error(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    app.run(debug=False)
