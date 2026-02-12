from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def principal():
    conexao = mysql.connector.connect(
        host="localhost",
        port=67,
        user="root",
        password="root",
        database="spotiduck"
    )

    # Vai entregar coluna nome é esse valor, ao inves de dar tudo separado em ma lista sem direcionamento 
    cursor = conexao.cursor(dictionary=True)

    # Comando

    cursor.execute("""
        

    """)




    return render_template('principal.html')

@app.route('/admin')
def admin():
    return render_template('administracao.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)