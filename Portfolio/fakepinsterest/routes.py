from flask import render_template
from flask_login import login_required
from fakepinsterest import app

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route("/usuario/<usuario>")
@login_required
def usuario(usuario):
    return render_template("usuario.html", usuario=usuario)

@app.route("/pesquisaexperiencia")
def pesquisa():
    return render_template("pesquisaexper.html")
