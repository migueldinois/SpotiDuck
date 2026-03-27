from flask import Flask, render_template, request, redirect, session, flash, url_for
import mysql.connector
from model.genero import Genero
from database.conexao import Conexao
from model.musica import Musica
from model.usuario import Usuario

app = Flask(__name__)

app.secret_key = "pato"

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
    if "usuario" in session:
        musicas = Musica.recuperar_musicas()
        generos = Genero.recuperar_generos()

        return render_template('administracao.html',  musicas = musicas, generos = generos)
    else:
        return redirect("/login")

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
    

@app.route("/cadastro")
def pagina_cadastro():
    if "usuario" in session:
        return redirect("/admin")
    return render_template("cadastro.html")

@app.route("/usuario/cadastro", methods=["POST"])
def criar_cadastro():
    input_usuario = request.form.get("usuario")
    input_senha = request.form.get("senha")
    
    if Usuario.cadastrar_usuario(input_usuario, input_senha):
        return redirect("/home")
    else:
        return "Erro ao cadastrar"

@app.route("/login")
def pagina_login():
    if "usuario" in session:
        return redirect("/admin")
    return render_template("login.html")
@app.route("/usuario/login", methods=["POST"])
def validar_login():
    input_usuario = request.form.get("usuario")
    input_senha = request.form.get("senha")
    usuario_logado = Usuario.autenticar_usuario(input_usuario, input_senha)

    if Usuario.autenticar_usuario(input_usuario, input_senha):
        session["usuario"] = usuario_logado
        flash(f"Bem vindo de volta {usuario_logado}!", "success")
        return redirect(url_for("admin"))
    else:
        flash("Usuario ou senha invalidos!", "error")
        return redirect('/login')

# Funcao para deslogar
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("usuario", None)
    return redirect("/home")



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)