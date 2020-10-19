from flask import render_template
from app import app
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



'''@app.route("/test/<int:id>")  # pelo id
def test(id):
    print(type(id))
    return ""'''


'''@app.route("/test", defaults={'name': None})  # sem nome por esta rota
@app.route("/test/<name>")  # com nome por esta rota
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, desconhecido!"'''
