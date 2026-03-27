from flask import request
from database.conexao import Conexao

class Musica():
    def recuperar_musicas():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, img_capa, nome, cantor, duracao, nome_genero, ativo FROM musicas')
        musicas = cursor.fetchall()

        return musicas
    
    def salvar_musica(nome_musica:str, cantor:str, duracao:str, url_imagem:str, genero:str) -> bool:
        '''
        Esta função ira servir para adicionar as músicas e conferir com o bool se realmente foi adicionada.

        '''
        try:

            conexao, cursor = Conexao.conectar()

            cursor.execute('''
                        
                        INSERT INTO `spotiduck`.`musicas` 

                        (cantor, duracao, nome, img_capa, nome_genero)
                        values (%s, %s, %s, %s,%s);

                        ''',

                        [ cantor, duracao, nome_musica, url_imagem, genero ]
                    
                        )
            
            conexao.commit()
            conexao.close()

            return True
        except:
            return False

    def excluir_musica(codigo:int) -> bool:
        '''
        Funcao pare excluir as musicas
        '''
        try:
            conexao, cursor = Conexao.conectar()
            
            cursor.execute('''
                DELETE FROM musicas 
                WHERE codigo = %s
            ''', 
            [codigo])   
            conexao.commit()   
            
            conexao.close() 

            return True
            
        except Exception as erro:
            print(erro)
            return False
        
    def alterar_status(status:int, codigo:int) -> bool:
        '''Serve para alterar o status da musica'''
        status = int(status)
        try:
            if status:
                conexao, cursor = Conexao.conectar()
                cursor.execute('''
                    UPDATE musicas
                    SET ativo = 0
                    WHERE codigo = %s
                ''', [codigo])
                
                conexao.commit()
                conexao.close()
                return True
            elif status == False: 
                conexao, cursor = Conexao.conectar()
                cursor.execute('''
                    UPDATE musicas
                    SET ativo = 1
                    WHERE codigo = %s
                ''', [codigo])
                
                conexao.commit()
                conexao.close()
                return True

            
        except Exception as erro:
            print(erro)
            return False

