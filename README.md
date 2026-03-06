# 🎵 SpotiDuck

SpotiDuck é uma aplicação web desenvolvida com **Flask** para gerenciar músicas, gêneros e usuários. O projeto utiliza **MySQL** como banco de dados e segue o padrão **MVC** (Model-View-Controller).

---

## 🛠️ Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---


---

## 🚀 Funcionalidades

- **Gerenciamento de Músicas**: Adicionar, listar, editar status e excluir músicas.
- **Gerenciamento de Gêneros**: Listar gêneros disponíveis.
- **Cadastro e Login de Usuários**: Criar contas e autenticar usuários.
- **Painel Administrativo**: Interface para gerenciar músicas e gêneros.

---

## 🌐 Rotas da Aplicação

### Rotas Públicas

| Método | Rota          | Descrição                                                                 |
|--------|---------------|---------------------------------------------------------------------------|
| GET    | `/` ou `/home`| Página principal com listagem de músicas e gêneros.                      |
| GET    | `/cadastro`   | Exibe o formulário de cadastro de usuários.                              |
| POST   | `/usuario/cadastro` | Realiza o cadastro de um novo usuário.                              |
| GET    | `/login`      | Exibe o formulário de login.                                             |
| POST   | `/usuario/login` | Realiza a autenticação do usuário.                                     |
| GET    | `/logout`     | Encerra a sessão do usuário.                                             |

### Rotas Administrativas (Protegidas)

| Método | Rota                  | Descrição                                                                 |
|--------|-----------------------|---------------------------------------------------------------------------|
| GET    | `/admin`              | Painel administrativo para gerenciar músicas e gêneros.                  |
| POST   | `/musica/post`        | Adiciona uma nova música ao banco de dados.                              |
| GET    | `/musica/delete/<id>` | Exclui uma música com base no ID.                                        |
| GET    | `/musica/status/<status>/<id>` | Altera o status (ativo/inativo) de uma música com base no ID. |

---

## 🗂️ Modelos

### `Genero`
- **Funções**:
  - `recuperar_generos`: Retorna todos os gêneros cadastrados no banco de dados.

### `Musica`
- **Funções**:
  - `recuperar_musicas`: Retorna todas as músicas cadastradas.
  - `salvar_musica`: Adiciona uma nova música ao banco de dados.
  - `excluir_musica`: Exclui uma música com base no código.
  - `alterar_status`: Altera o status (ativo/inativo) de uma música.

### `Usuario`
- **Funções**:
  - `cadastrar_usuario`: Realiza o cadastro de um novo usuário.
  - `autenticar_usuario`: Verifica se o usuário e senha estão corretos.

---

## 🛠️ Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/migueldinois/SpotiDuck
   cd spotiduck