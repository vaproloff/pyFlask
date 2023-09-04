# Задание No4
# 📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
#    ○ Имя пользователя (обязательное поле)
#    ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
#    ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
#    ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# 📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
#    и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не заполнено
#    или данные не прошли валидацию, то должно выводиться соответствующее сообщение об ошибке.
# 📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в базе данных.
#    Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.

from flask import Flask, render_template, request
from flask_wtf import CSRFProtect

from models import db, User
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = b'2bc64352e8d6be54e518a6731e4a9e8330eee6130559ed5fb6c779bab3f88e3d'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Вы успешно зарегистрированы'
    return render_template('register.html', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/users/')
def index():
    users = User.query.all()
    return str(list(users))


if __name__ == '__main__':
    app.run(debug=True)
