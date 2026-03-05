from flask import Flask, render_template, request, redirect
from database.conexao import Conexao

class Genero():
    def recuperar_generos():
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT nome, url_icone, cor FROM genero")
        generos = cursor.fetchall()

        return generos
