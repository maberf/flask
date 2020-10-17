from flask import render_template
from app import app


@app.route("/index/<user>")
@app.route("/", defaults={"user": None})
def index(user):
    return render_template('index.html', user=user)  # variavel user




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
