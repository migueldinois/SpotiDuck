from flask import request
from database.conexao import Conexao

class Musica():
    def recuperar_musicas():
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT codigo, img_capa, nome, cantor, duracao, nome_genero FROM musicas")
        musicas = cursor.fetchall()

        return musicas
    
    def adicionar_musica():

        input_titulo = request.form.get("titulo-musica")
        input_cantor = request.form.get("cantor-musica")
        input_duracao = request.form.get("duracao-musica")
        input_imagem = request.form.get("imagem_musica")
        input_genero = request.form.get("categoria-musica")

        conexao, cursor = Conexao.conectar()
        
        #  no mysql utilizamos %s para variaveis assim, e no sqlite utilizamos "?"
        cursor.execute("""

            INSERT INTO `spotiduck`.`musicas` 
            (`img_capa`, `nome`, `cantor`, `duracao`, `nome_genero`) 
            VALUES 
            ("%s", 
            "%s", 
            "%s", 
            "%s",
            "%s")

            """, (input_titulo, input_cantor, input_duracao, input_imagem, input_genero))
        
        conexao.commit()

