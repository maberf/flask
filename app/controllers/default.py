from flask import render_template
from app import app, db
from app.models.tables import User
from app.models.forms import LoginForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()  # instância na página de login
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html', form=form)


@app.route("/test/<info>")  # página de teste de inserção no BD
@app.route("/test/", defaults={'info': None})
def test(info):
    i = User("uiliam", "1234", "Uiliam Zeferino", "uiliamzeferino@hotmail.com")
    db.session.add(i)  # abre sessão no BD para inserção de instância i
    db.session.commit(i)  # grava (persiste) no BD a inserção da instância i
    return "OK"
    