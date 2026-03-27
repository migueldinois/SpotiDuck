import mysql.connector
tipo_conexao = "NUVEM"
class Conexao():
    @staticmethod
    def conectar():
        if tipo_conexao == "NUVEM":
            conexao = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="spotiduck")
        else:
            conexao = mysql.connector.connect(
            host="mysql-16a29790-spotiduck.j.aivencloud.com",
            port=15558,
            user="avnadmin",
            password="AVNS_vnjO12YffaAjPXcHpC0",
            database="SpotiDuck")

        # Vai entregar coluna nome é esse valor, ao inves de dar tudo separado em ma lista sem direcionamento 
        cursor = conexao.cursor(dictionary=True)
        return conexao, cursor
