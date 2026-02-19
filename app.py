from flask import Flask, render_template, request
import mysql.connector
from model.genero import Genero
from database.conexao import Conexao
from model.musica import Musica

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def principal():

    # Pegando conexao e cursor da classe
    conexao, cursor = Conexao.conectar()

    # Recuperando Musicas
    musicas = musicas = Musica.recuperar_musicas()

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

@app.route('/salvar_musica', methods=['POST'])
def salvar_musica():
    
    Musica.adicionar_musica()
    return render_template('administracao.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)