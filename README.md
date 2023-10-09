# Sistema de Cadastro e Login

Este é um simples sistema de cadastro e login em Python usando a biblioteca customtkinter e um banco de dados SQLite.

## Funcionalidades

- **Cadastro de Usuário**: Os usuários podem se cadastrar fornecendo seu nome, email e senha. A senha é armazenada com segurança no banco de dados.

- **Login de Usuário**: Os usuários registrados podem fazer login usando seu email e senha. O sistema verifica as credenciais no banco de dados.

- **Interface Gráfica Personalizada**: A interface gráfica é criada usando a biblioteca customtkinter, tornando-a atraente e amigável.

- **Armazenamento de Dados**: As informações do usuário são armazenadas em um banco de dados SQLite.

## Pré-requisitos

Antes de executar o sistema, certifique-se de que você tenha os seguintes requisitos instalados:

- Python 3.x
- Biblioteca customtkinter
- SQLite

## Instalação

1. Clone este repositório em sua máquina local:

    git clone https://github.com/seu-usuario/seu-repositorio.git

2. Instale a biblioteca customtkinter usando o seguinte comando:
   
   pip install customtkinter
   
## Executando o Sistema

Para executar o sistema, use os seguintes comandos:

```python
# Para criar o banco de dados
python conexao.py

# Para iniciar o programa
python tela.py
