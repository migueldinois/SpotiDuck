import mysql.connector

class Conexao():
    
    @staticmethod
    def conectar():
        conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="spotiduck"
    )

        # Vai entregar coluna nome é esse valor, ao inves de dar tudo separado em ma lista sem direcionamento 
        cursor = conexao.cursor(dictionary=True)
        return conexao, cursor