from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def principal():
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="spotiduck"
    )

    # Vai entregar coluna nome é esse valor, ao inves de dar tudo separado em ma lista sem direcionamento 
    cursor = conexao.cursor(dictionary=True)

    # Comando

    cursor.execute("SELECT codigo, img_capa, nome, cantor, duracao, nome_genero FROM musicas")
    
    # Guardando os dados em uma variavel
    musicas = cursor.fetchall()
    # Fechou a conexao
    conexao.close()




    return render_template('principal.html', musicas = musicas)

@app.route('/admin')
def admin():
    return render_template('administracao.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)