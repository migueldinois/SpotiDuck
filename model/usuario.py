from database.conexao import Conexao
from flask import Flask, render_template, request, redirect, session

class Usuario():
    def cadastrar_usuario(usuario: str, senha: str):
        """Função para cadastro de usuario"""
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""
                        
                        INSERT INTO `spotiduck`.`usuarios` 

                        (usuario, senha, administrador)
                        values (%s, %s, %s);

                        """,

                        [usuario, senha, "0"]
                    
                        )
            
            conexao.commit()
            conexao.close()
            
            return True
        except Exception as erro:
            print(erro)
            return False
        
    def autenticar_usuario(usuario_input: str, senha_input: str):
        """Função que verifica se o usuario existe e se estiver cadastrado retorna true, caso contrrio retorna false"""
        conexao, cursor = Conexao.conectar()
        cursor.execute("SELECT usuario FROM usuarios WHERE usuario = %s AND senha = %s", [usuario_input, senha_input])
        
        usuario = cursor.fetchone() 
        # Se o usuario não for nulo, vai entrar com essa session
        if usuario is not None:
            try:
                return True
            except Exception as erro:
                print(erro)
                return False
                