import subprocess
import multiprocessing
from flask import Flask, render_template

# Definindo o app Flask
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

# Função para rodar o Flask
def run_flask():
    app.run(debug=True, use_reloader=False, port=5001)  # Flask na porta 5001

# Função para rodar o Streamlit
def run_streamlit():
    subprocess.run(["streamlit", "run", "main.py"])  # Assumindo que o arquivo principal do Streamlit é 'main.py'

if __name__ == "__main__":
    # Criando processos separados para Flask e Streamlit
    flask_process = multiprocessing.Process(target=run_flask)
    streamlit_process = multiprocessing.Process(target=run_streamlit)

    # Inicia os dois processos
    flask_process.start()
    streamlit_process.start()

    # Aguarda o término de ambos os processos
    flask_process.join()
    streamlit_process.join()
