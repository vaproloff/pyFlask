# Задание No5
# 📌 Создать форму регистрации для пользователя.
# 📌 Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения,
#    согласие на обработку персональных данных.
# 📌 Валидация должна проверять, что все поля заполнены корректно
#    (например, дата рождения должна быть в формате дд.мм.гггг).
# 📌 При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.

# Задание No6
# 📌 Дополняем прошлую задачу.
# 📌 Создайте форму для регистрации пользователей в вашем веб-приложении.
# 📌 Форма должна содержать следующие поля: имя пользователя, электронная почта, пароль и подтверждение пароля.
# 📌 Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
# 📌 После отправки формы, выведите успешное сообщение об успешной регистрации.

# Задание No7
# 📌 Создайте форму регистрации пользователей в приложении Flask.
#    Форма должна содержать поля: имя, фамилия, email, пароль и подтверждение пароля.
#    При отправке формы данные должны валидироваться на следующие условия:
#       ○ Все поля обязательны для заполнения.
#       ○ Поле email должно быть валидным email адресом.
#       ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
#       ○ Поле подтверждения пароля должно совпадать с полем пароля.
#       ○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
#       ○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.

# Задание No8
# 📌 Создать форму для регистрации пользователей на сайте.
# 📌 Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# 📌 При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

import hashlib

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect

from models import db, User
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = b'2bc64352e8d6be54e518a6731e4a9e8330eee6130559ed5fb6c779bab3f88e3d'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Main page'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = hashlib.sha256(form.password.data.encode()).hexdigest()
        date_of_birth = form.date_of_birth.data
        user = User(username=username, email=email, password=password, date_of_birth=date_of_birth)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html', form=form)


@app.route('/success/')
def success():
    return 'Вы успешно зарегистрированы!'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('DB created')


if __name__ == '__main__':
    app.run(debug=True)
