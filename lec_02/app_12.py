from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'3891f989b75a5b6e8f5f8cab6d1431b865a05acc126ff7e1cae4ce028df65413'


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        flash('Форма успешно отправлена', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
