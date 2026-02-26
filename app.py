from flask import Flask, render_template, request, redirect
import mysql.connector
from model.genero import Genero
from database.conexao import Conexao
from model.musica import Musica

app = Flask(__name__)


lista_de_musicas = []

@app.route('/')
@app.route('/home')
def principal():

    # Pegando conexao e cursor da classe
    conexao, cursor = Conexao.conectar()

    # Recuperando Musicas
    musicas = Musica.recuperar_musicas()
    
    

    # Recuperando Generos
    generos = Genero.recuperar_generos()

    # Fechou a conexao
    conexao.close()

    return render_template('principal.html', musicas = musicas, generos = generos)

@app.route('/admin')
def admin():

    musicas = Musica.recuperar_musicas()
    generos = Genero.recuperar_generos()

    return render_template('administracao.html',  musicas = musicas, generos = generos)

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    input_titulo = request.form.get("titulo-musica")
    input_cantor = request.form.get("cantor-musica")
    input_duracao = request.form.get("duracao-musica")
    input_imagem = request.form.get("imagem_musica")
    input_genero = request.form.get("categoria-musica")
    


    if Musica.salvar_musica(input_titulo, input_cantor, input_duracao, input_imagem, input_genero ):

        return redirect("/admin")
    else:
        return "Erro ao adicionar música"


@app.route("/musica/delete/<codigo>")
def delete_musica(codigo):
    if Musica.excluir_musica(codigo):
        return redirect("/admin")
        
    else:
        return "Erro ao excluir  música"


@app.route("/musica/status/<status>/<codigo>")
def alterar_status_musica(status, codigo):

    if Musica.alterar_status(status, codigo):
        return redirect("/admin")
    else:
        return "Erro ao alterar  música"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)