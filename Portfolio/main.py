from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route("/usuario/<usuario>")
def usuario(usuario):
    return render_template("usuario.html", usuario=usuario)

@app.route("/pesquisaexperiencia")
def pesquisa():
    return render_template("pesquisaexper.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5001)  # Mudando a porta para 5001
