from flask import Flask, render_template, url_for

app = Flask(__name__)

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
