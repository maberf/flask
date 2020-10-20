from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db, login_manager
from app.models.tables import User
from app.models.forms import LoginForm


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()  # instância na página de login
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  
        if user and user.password == form.password.data:
        # se usuário existe e a senha digitada confere com o valor no BD
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))  # após login vai para index
        else:
            flash("Invalid login.")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))  # após logout vai para index

"""
@app.route("/test/<info>")  # teste do BD
@app.route("/test/", defaults={"info": None})
def test(info):
    r = User.query.filter_by(username="uiliam").first()  # lê BD
    db.session.delete(r)  # deleta registro do BD
    db.session.commit()  # comita (persiste) no BD
    return "OK"
"""