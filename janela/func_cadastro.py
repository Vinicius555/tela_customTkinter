from conexao import error, curso, conn
import re
import hashlib


valida_email = "[a-zA-Z_\d\.]+@[a-zA-Z_\d]+\.com(?:\.\w\w){0,1}"
nome_padrao = r"^[a-zA-Z]+( [a-zA-Z]+)*$"


class Register():
    def __init__(self, name, email, password, confirm_password):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password


class CreateRegister:
    @staticmethod
    def create_register(name, email, password, confirm_password):
        try:
            if not re.match(nome_padrao, name):
                return False, "Nome inválido"

            if not re.match(valida_email, email):
                return False, "Email inválido."

            if len(password) < 6:
                return False, "Senha muito curta!"

            if password != confirm_password:
                return False, "As Senhas não coincidem!"
            else:
                sha256 = hashlib.sha256()
                password_bytes = password.encode('utf-8')
                sha256.update(password_bytes)
                hashed_password = sha256.hexdigest()
                curso.execute(
                    f"INSERT INTO usuarios VALUES (NULL, '{name}', '{email}', '{hashed_password}')")
                conn.commit()

            return True, None
        except error as er:
            print(er)