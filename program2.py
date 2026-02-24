from flask import Flask, render_template, redirect
from forms import EmergencyAccess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

profs = [
    "инженер-исследователь",
    "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию", "климатолог",
    "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения", "метеоролог",
    "оператор марсохода"
]


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Домашняя страница'
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training(prof):
    params = {
        'title': 'Тренировки',
        'prof': prof
    }
    return render_template('training.html', **params)


@app.route('/list_prof/<list_p>')
def list_prof(list_p):
    params = {
        'title': 'Тренировки',
        'list_p': list_p,
        'prof_list': profs
    }
    return render_template('list_prof.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = EmergencyAccess()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return 'Авторизация успешна'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
